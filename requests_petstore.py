import data
import requests


url = data.PETS_URL
headers = data.request_headers
body = data.request_body


#requests for PET section (Everything about your pets)
def create_body(id, name):
    body["id"] = id
    body["name"] = name
    return body


def create_pet(id, name):
    create_body(id, name)
    response = requests.post(url=url, headers=headers, json=body)
    return response


def get_pet(id):
    response = requests.get(url=url + str(id), headers=headers)
    return response


def update_pet(id, name):
    create_body(id, name)
    response = requests.put(url=url, headers=headers, json=body)
    return response


def delete_pet(id):
    try:
        response = requests.delete(url=url + str(id), headers=headers)
        return response
    except:
        print("Pet doesn't exist!")


def validate_response(response):
    assert (type(response["id"])) == int
    assert (type(response["category"])) == dict
    assert (type(response["category"]["id"])) == int
    assert (type(response["category"]["name"])) == str
    assert (type(response["name"])) == str
    assert (type(response["photoUrls"])) == list
    for i in (response["photoUrls"]):
        assert (type(i)) == str
    assert (type(response["tags"])) == list
    assert (type(response["tags"][0])) == dict
    assert (type(response["tags"][0]["id"])) == int
    assert (type(response["tags"][0]["name"])) == str
    assert (type(response["status"])) == str


