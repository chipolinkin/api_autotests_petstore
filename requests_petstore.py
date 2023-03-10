import data
import requests


url = data.PETS_URL
headers = data.request_headers
body = data.request_body


# requests for PET section (Everything about your pets)
def create_body(pet_id, pet_name):
    body["id"] = pet_id
    body["name"] = pet_name
    return body


def create_pet(pet_id, pet_name):
    create_body(pet_id, pet_name)
    response = requests.post(url=url, headers=headers, json=body)
    return response


def get_pet(pet_id):
    response = requests.get(url=url + str(pet_id), headers=headers)
    return response


def update_pet(pet_id, pet_name):
    create_body(pet_id, pet_name)
    response = requests.put(url=url, headers=headers, json=body)
    return response


def delete_pet(pet_id):
    try:
        response = requests.delete(url=url + str(pet_id), headers=headers)
        return response
    except Exception as e:
        print(f"ERROR {e}, Pet doesn't exist!")


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
