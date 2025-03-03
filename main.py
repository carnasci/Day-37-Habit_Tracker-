import requests
from datetime import datetime
from credentials import pixela_params, pixela_token, username

pixela_endpoint = "https://pixe.la/v1/users"
graph = "graph1"

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

add_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph}"
today = datetime.now()
date = today.strftime("%Y%m%d")
print(date)
add_pixel_params = {
    "date" : date,
    "quantity" : "3.75",
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)

put_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph}/{date}"
put_params = {
    "quantity" : "3.75"
}
# response = requests.put(url=put_pixel_endpoint, json=put_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph}/{date}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)