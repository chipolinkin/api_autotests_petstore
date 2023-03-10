import pytest
import data


@pytest.fixture
def id_pet():
    id_pet = data.generate_pet_id()
    return id_pet


@pytest.fixture
def name_pet():
    name_pet = data.pet_name
    return name_pet
