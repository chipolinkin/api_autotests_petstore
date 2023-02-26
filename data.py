import random


def generate_pet_id():
    generate_pet_id = random.randint(1, 9999)
    return generate_pet_id


PETS_URL = "https://petstore.swagger.io/v2/pet/"


request_headers = {
    'api-key': 'special-key',
    'Content-Type': 'application/json'
    }


pet_name = "Simba"

request_body = {
    "id": generate_pet_id(),
    "category": {
        "id": generate_pet_id()+2,
        "name": "string"
    },
    "name": pet_name,
    "photoUrls": [
        "https://imagefortest.com/pic.jpg"
    ],
    "tags": [
        {
            "id": generate_pet_id()+3,
            "name": "TAG3"
        }
    ],
    "status": "available"
}
