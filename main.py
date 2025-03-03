import requests
from credentials import pixela_params, pixela_token, username

pixela_endpoint = "https://pixe.la/v1/users"

#response = requests.post(url=pixela_endpoint, json=pixela_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Hours Coding",
    "unit" : "hours",
    "type" : "float",
    "color" : "ichou"
}

headers = {
    "X-USER-TOKEN" : pixela_token,
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

add_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/graph1"
date = "20250303"
add_pixel_params = {
    "date" : date,
    "quantity" : "3.5",
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)