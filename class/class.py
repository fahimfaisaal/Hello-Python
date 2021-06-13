import json


class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    # public method
    def can_walk(self):
        return f"{self.name} can walk."

    # private method
    def __have_acc(self):
        return f"{self.name} has an account."

if __name__ == '__main__':
    person = Person("fahim", 22, "Rajshahi")
    person2 = Person("shakil", 18, "Naogaon")

    print(person.__dict__, person2.__dict__)
