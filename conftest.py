import pytest
import data
import requests_petstore

@pytest.fixture
def idpet():
    idpet = data.generate_pet_id()
    return idpet

@pytest.fixture
def namepet():
    namepet = data.pet_name
    return namepet

