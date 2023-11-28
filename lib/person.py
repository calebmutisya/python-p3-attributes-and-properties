#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        if name =="":
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif len(str(name))> 25:
            print("Name must be string between 1 and 25 characters.")
        elif not 1<= len(str(name)) <=25:
            self.name = name.title()
        
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self.job = job
        
guido = Person("Guido","ITC")