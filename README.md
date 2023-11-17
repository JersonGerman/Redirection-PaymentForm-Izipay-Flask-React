# Redirection-PaymentForm-Izipay-Flask-React

## Requirements
* Python v3.7.6  or higher
+ Nodejs v18.15.0 or higher

## Configuration
Change with your Izipay keys in the `flask-server` folder in the `keys.py` file
```py
KEY = {
    "SHOP_ID": 12345678,
    "CLAVE": "AN7sPAUn19UQ1cXL"
}
```

Install libraries for the backend and frontend in each folder or run the following command
```sh
node index.js
```
Run local servers for each project
```sh
cd flask-server
py main.py
```
```sh
cd fronted
npm run dev
```