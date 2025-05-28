import pytest
from owner_pet import Owner, Pet

def test_owner_can_add_pet():
    owner = Owner("Alice")
    pet = Pet("Buddy", "dog")
    owner.add_pet(pet)
    assert pet in owner.pets()

def test_pet_removal():
    pet = Pet("Buddy", "dog")
    pet.remove()
    assert pet not in Pet.all