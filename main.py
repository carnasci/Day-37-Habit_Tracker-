import requests
from credentials import pixela_params

pixela_endpoint = "https://pixe.la/v1/users"

response = requests.post(url=pixela_endpoint, json=pixela_params)
print(response.text)