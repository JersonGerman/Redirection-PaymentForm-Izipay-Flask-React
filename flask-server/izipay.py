import hmac
import base64
import hashlib
import random
import string
from datetime import datetime, timedelta

def initForm():
    return {
        "vads_action_mode": "INTERACTIVE",
        "vads_amount": 0,
        "vads_ctx_mode": "TEST",
        "vads_currency": "604",
        "vads_order_id": "",
        "vads_page_action": "PAYMENT",
        "vads_payment_config": "SINGLE",
        "vads_site_id": 12345678,
        "vads_trans_date": 20231101123000,
        "vads_trans_id": "adf21h",
        "vads_version": "V2",
        "vads_cust_first_name": "Jerson",
        "vads_cust_last_name": "German"
    }

def get_signature(params, key):
    
    #"Function that computes the signature.
    #params : dictionary containing the fields to send in the payment form.
    #key : TEST or PRODUCTION key
    # Initialization of the variable that will contain the string to encrypt
    signature_content = ""

    # Sorting fields alphabetically
    sorted_params = dict(sorted(params.items()))

    for name, value in sorted_params.items():
        # Recovery of vads_ fields
        if name.startswith('vads_'):
            # Concatenation with "+"
            signature_content += str(value) + "+"

    # Adding the key at the end
    signature_content += key

    # Encoding base64 encoded chain with SHA-256 algorithm
    signature = base64.b64encode(hmac.new(key.encode(), msg=signature_content.encode(), digestmod=hashlib.sha256).digest())
    
    return signature.decode()

def getDateFormat():
    # Obtén la hora actual en Perú
    now = datetime.now()

    # Añade 5 horas para obtener la hora UTC
    utc_time = now + timedelta(hours=5)

    # Formatea la fecha y hora en el formato AAAAMMDDHHMMSS
    formatted_date = utc_time.strftime('%Y%m%d%H%M%S')

    return formatted_date

def generate_unique_id():
    # Genera una cadena de 6 caracteres que incluye números y letras minúsculas
    unique_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
    return unique_string
