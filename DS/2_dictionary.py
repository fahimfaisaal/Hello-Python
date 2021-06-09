# Dictionary
person = {
    "name": "fahim faisal",
    "age": 22,
    "location": "Rajshahi-Bangladesh",
    "skills": ["C", "java", "javaScript"]
}

print(person)

# Access by key with list notation
print(person["name"])
print(person["skills"])

# Access by key with get method
print(person.get("location"))
print(person.get("married", "Not valid key!"))

# Dictionary key can be digit also
student_ID = {
    101: {
        "name": "fahim faisal",
        "age": 22,
        "location": "Rajshahi"
    },
    102: {
        "name": "Shakil",
        "age": 18,
        "location": "Naogaon"
    },
    103: {
        "name": "Truky",
        "age": 24,
        "location": "Barisal"
    },
    104: {
        "name": "Ashraful Islam",
        "age": 27,
        "location": "BrammonBaria"
    }
}

print(student_ID.pop(102))
print(student_ID.get(104))