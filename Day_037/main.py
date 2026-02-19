import requests
from datetime import datetime


USERNAME = "thomas-dev"
TOKEN ='hjqw12ja2eer9b1l35lx92aq1'
GRAPH_ID="graph1"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}
user_params = {
    "token": 'hjqw12ja2eer9b1l35lx92aq1',
    "username": "thomas-dev",
    "agreeTermsOfService":"yes",
    "notMinor": "yes",
}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Study Minutes",
    "unit": "min",
    "type": "int",
    "color": "shibafu",
}
# response=requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)
graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# custom_date = datetime(year=2026, month=1, day=7)


pixel_data = {
"date":	today.strftime("%Y%m%d"),     # string 	[required] The date on which the quantity is to be recorded. It is specified in yyyyMMdd format.
"quantity":	"120", 	    # [required] Specify the quantity to be registered on the specified date. Validation rule: int ^\-?[0-9]+, float ^\-?[0-9]+\.[0-9]+
"optionalData":"",      # string
}
# response = requests.post(url=graph_update_endpoint,json=pixel_data, headers=headers)
# print(response.text)



# # Use PUT to change settings
# update_config = {
#     # "color": "ajisai",  # purple
#     # "color": "sora",    # blue
#     # "color": "shibafu", # green
#     "color": "momiji",  # red
#     # "color": "ichou",   # yellow
#     # "color": "kuro",    # black
# }
# response = requests.put(url=graph_update_endpoint, json=update_config, headers=headers)
# print(response.text)