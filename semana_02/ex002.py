import requests
from requests.exceptions import RequestException, Timeout

class HTTPClient:
    def __init__(self, headers=None, timeout=5):
        self.headers = headers if headers else {}
        self.timeout = timeout

    def get(self, url, params=None):
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
            return response.text
        except Timeout:
            return "erro de timeout"
        except RequestException as e:
            return f"erro na requisição, erro: {e}"
        
    def post(self, url, data=None, json=None):
        try:
            response = requests.post(url, headers=self.headers, timeout=self.timeout, data=data, json=json)
            return response.text
        except Timeout:
            return "erro de timeout"
        except RequestException as e:
            return f"erro na requisição, erro: {e}"
        

client = HTTPClient()
response = client.get('https://www.google.com.br/?hl=pt-BR')
print(response)
response = client.post("https://jsonplaceholder.typicode.com/posts", json={"teste": "teste"})
print(response)