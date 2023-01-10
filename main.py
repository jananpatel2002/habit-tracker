import requests
import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = "janan"
TOKEN = "1hj23nj1SJJALsZJ(((2(#_!@$ZSS"
GRAPHID = "graph1"
date = datetime.datetime.now()
print(date)

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_parameters = {
    "id": "graph1",
    "name": "Coding Hours Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"

}
pixel_posting_parameters = {
    "date": date,
    "quantity": "1.5",
}
pixel_updating_parameters = {
    "quantity": "1",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date.strftime('%Y%m%d')}"

# Initially creating the user

# response = requests.post(pixela_endpoint, json=parameters)
# print(response.text)


# Post request to post a pixel

# response = requests.post(graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)
#
# response = requests.post(graph_endpoint, json=pixel_posting_parameters, headers=headers)
# print(response.text)

# Updating the pixels

# response = requests.put(graph_endpoint, json=pixel_updating_parameters, headers=headers)
# print(response.text)

# Deleting a post


# response = requests.delete(graph_endpoint, headers=headers)
# print(response.text)
