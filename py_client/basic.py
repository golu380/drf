import requests

endpoint = "http://localhost:8000/api/"
endpoints1 = "http://localhost:8000/api/postcheck"
get_response = requests.get(endpoint, params={"abc":123}, json={"query":"hello world"})
get_responsepost = requests.post(endpoints1, params={"abc":123}, json={"title":"Amit Kumar Dubey"})



# print(get_response.text)
# print(get_response.headers)
# print(get_response.status_code)
# print(get_response.json()['message'])
# print(get_response.json())
print(get_responsepost.json())
print(get_response.json())

# HTTP Request -> html
# REST API HTTP Request -> Json (xml)