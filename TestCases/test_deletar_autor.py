import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Authors/3344"

def test_deletando_autor():
    response = requests.delete(url)

    assert response.status_code == 200
    print('STATUS CODE =', response.status_code)
