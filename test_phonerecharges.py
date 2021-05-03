import requests


BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "PhoneRecharges/1", {'company_id': 'claro_11', 'product_id': 'claro_10', 'value': 10.0, 'phone_number': 5511999999999})
print('POST /PhoneRecharges/1')
print(response.json())
print('')

response = requests.put(BASE + "PhoneRecharges/2", {'company_id': 'claro_99', 'product_id': 'claro_10', 'value': 10.0, 'phone_number': 5511999999999})
print('POST /PhoneRecharges/2 - 409: empresa nao existe')
print(response.json())
print('')

response = requests.put(BASE + "PhoneRecharges/2", {'company_id': 'claro_11', 'product_id': 'claro_99', 'value': 10.0, 'phone_number': 5511999999999})
print('POST /PhoneRecharges/2 - 409: produto nao existe')
print(response.json())
print('')

response = requests.put(BASE + "PhoneRecharges/2", {'company_id': 'claro_11', 'product_id': 'claro_20', 'value': 20.0, 'phone_number': 5511999999999})
print('POST /PhoneRecharges/2 - Nova recarga com mesmo numero')
print(response.json())
print('')
