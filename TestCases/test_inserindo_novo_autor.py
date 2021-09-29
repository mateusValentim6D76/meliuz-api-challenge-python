import requests
import json

url = "https://fakerestapi.azurewebsites.net/api/v1/Authors/"

def test_inserir_novo_autor():

    payload = json.dumps({
      "id": "33667",
      "idBook": "699",
      "firstName": "Mateus704",
      "lastName": "Valentim"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200
    print('STATUS CODE = ',response.status_code)

    print(response.text)