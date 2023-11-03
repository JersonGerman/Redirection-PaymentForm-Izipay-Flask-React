from flask import Flask, jsonify, request, json
from flask_cors import CORS
from urllib.parse import unquote, parse_qs

from izipay import initForm, getDateFormat, generate_unique_id, get_signature
from keys import KEY

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def root():
    return "Home"

@app.route('/paymentForm', methods=['POST'])
def create_paymentForm():
    data = request.get_json()

    paymentConfig = initForm()
    paymentConfig["vads_amount"] = int(data["amount"]) * 100
    paymentConfig["vads_cust_first_name"] = data["firstName"]
    paymentConfig["vads_cust_last_name"] = data["lastName"]
    paymentConfig["vads_order_id"] = generate_unique_id() + getDateFormat()
    paymentConfig["vads_site_id"] = KEY["SHOP_ID"]
    paymentConfig["vads_trans_date"] = getDateFormat()
    paymentConfig["vads_trans_id"] = generate_unique_id()
    paymentConfig["signature"] = get_signature(params=paymentConfig, key=KEY["CLAVE"])
    
    return jsonify(paymentConfig), 201


@app.route('/ipn', methods=['POST'])
def  ipn():
    data = request.get_data().decode('utf-8') # Decodifica los datos a una cadena
    parsed_data = parse_qs(data)

    # Extrae la cadena JSON de 'kr-answer' 
    kr_hash_key = unquote(parsed_data.get('kr-hash-key')[0])
    kr_hash_algorithm =  unquote(parsed_data.get('kr-hash-algorithm')[0])
    kr_hash = unquote(parsed_data.get('kr-hash')[0])
    kr_anwer = unquote(parsed_data.get('kr-answer')[0])
    
    # Convierte la cadena JSON en un objeto Python
    json_answer = json.loads(kr_anwer)
    
    print("kr_hash", kr_hash)
    print("kr_hash_key", kr_hash_key)
    print("kr_hash_algorithm", kr_hash_algorithm)

    # Imprime el objeto Python
    # 
    print(json_answer['orderStatus'])  

    return "Transaccion is PAID!", 200

if __name__ == '__main__':
    app.run(debug=True)
