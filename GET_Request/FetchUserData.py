import jsonpath
import requests
import json
#API URL
url = "https://fakerestapi.azurewebsites.net/api/v1/Authors"

#Enviar Requisição GET
response  = requests.get(url)

#Mostrando conteúdo da resposta
json_response = json.loads(response.text)
print(json_response)

assert response.status_code == 200
print("Status Code: ", response.status_code)