import requests_petstore
import json
import allure


@allure.story('Creating a pet')
def test_create_pet(id_pet, name_pet):
    # create pet
    newpet = requests_petstore.create_pet(id_pet, name_pet)
    assert newpet.status_code == 200
    # deserialize json
    newpet = json.loads(newpet.content)
    # check data of response
    requests_petstore.validate_response(newpet)
    assert newpet["id"] == id_pet
    assert newpet["name"] == name_pet
    # delete the pet after test
    requests_petstore.delete_pet(id_pet)


@allure.story('Checking an existing pet')
def test_check_pet_via_get_request(id_pet, name_pet):
    pet = requests_petstore.create_pet(id_pet, name_pet)
    assert pet.status_code == 200
    getpet = requests_petstore.get_pet(id_pet)
    assert getpet.status_code == 200
    getpet = json.loads(getpet.content)
    requests_petstore.validate_response(getpet)
    assert getpet["id"] == id_pet
    assert getpet["name"] == name_pet
    requests_petstore.delete_pet(id_pet)


@allure.story('Updating a pet')
def test_update_pet_via_put_request(id_pet, name_pet):
    pet = requests_petstore.create_pet(id_pet, name_pet)
    assert pet.status_code == 200
    updpet = requests_petstore.update_pet(id_pet, "Harold")
    assert updpet.status_code == 200
    updpet = json.loads(updpet.content)
    requests_petstore.validate_response(updpet)
    assert updpet["id"] == id_pet
    assert updpet["name"] == "Harold"
    requests_petstore.delete_pet(id_pet)


@allure.story('Deleting a pet')
def test_delete_pet(id_pet, name_pet):
    newpet = requests_petstore.create_pet(id_pet, name_pet)
    assert newpet.status_code == 200
    get_newpet = requests_petstore.get_pet(id_pet)
    assert newpet.content == get_newpet.content
    delpet = requests_petstore.delete_pet(id_pet)
    assert delpet.status_code == 200
    non_existent_pet = requests_petstore.get_pet(id_pet)
    assert non_existent_pet.status_code == 404


# negative tests for pet section of the store
@allure.story('Checking a non-existent pet')
def test_get_request_non_exist_pet():
    pet = requests_petstore.get_pet("909090192")
    assert pet.status_code == 404


@allure.story('Trying to delete a non-existent pet')
def test_delete_non_exist_pet():
    pet = requests_petstore.delete_pet("923400292")
    assert pet.status_code == 404
