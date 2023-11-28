#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=''):
        if name == "":
            print("Name must be string between 1 and 25 characters.")
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        if len(str(name))>25:
            print("Name must be string between 1 and 25 characters.")
        if 1<= len(str(name)) <= 25:
            self.name=name 
            print(f"{name} Approved")
            
        
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed= breed
            print(f"{breed} Approved")

figo=Dog("Figo","Pug")

