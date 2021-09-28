import json
import requests

headers = {
    'Content-type':'application/json',
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive'
}

#API URL
url = "https://fakerestapi.azurewebsites.net/api/v1/Authors"

#Ler e escrever o Json file
file = open('C:\\Users\\mateus.oliveira\\PycharmProjects\\FakeRestApi\\JsonData\\createUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

#Requisicao POST
response = requests.post(url, request_json)

#assert response.status_code == 201

#Fetch header from response
print(response.headers)

#Parse response to Json format
response_json = json.loads(response.text)
