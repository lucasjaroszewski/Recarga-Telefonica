import requests

BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "CompanyProducts/" + str('claro_11'))
print('GET /CompanyProducts/claro_11')
print(response.json())
print('')

response = requests.get(BASE + "CompanyProducts/")
print('GET /CompanyProducts/')
print(response.json())
print('')

response = requests.patch(BASE + 'CompanyProducts/' + str('claro_11'), {'company_id': 'claro_12'})
print('PATCH /CompanyProducts/claro_11 -> {"company_id": "claro_12"}')
print(response.json())
print('')

response = requests.put(BASE + 'CompanyProducts/' + str('claro_13'), {'company_id': 'claro_13'})
print('PUT /CompanyProducts/claro_13')
print(response.json())
print('')

response = requests.delete(BASE + 'CompanyProducts/' + str('tim_11'))
print('DELETE /CompanyProducts/tim_11')
print({'message': 'Empresa deletada com sucesso'})
print('')
