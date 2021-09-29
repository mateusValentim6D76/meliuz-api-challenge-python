import requests
import json

url = "https://fakerestapi.azurewebsites.net/api/v1/Authors/113211?id=7777"

def test_atualiza_dados_autor():

  payload = json.dumps({
    "id": 3333,
    "idBook": 3,
    "firstName": "Mateus704",
    "lastName": "Valentim"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  print(response.text)
