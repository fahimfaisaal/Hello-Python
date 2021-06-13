import json

my_objects = [
    {
        "name": "fahim",
        "gmail": "fahimfaisal.soikot@gmail.com",
        "phone": "01823432434",
        "location": "Rajshahi",
        "socials": [
            {
                "name": "Facebook",
                "url": "https://www.facebook.com/fahimfaisaal"
            }, {
                "name": "Github",
                "url": "https://www.github.com/fahimfaisaal"
            }
        ]
    }, {
        "name": "Shakil",
        "gmail": "shakil@gmail.com",
        "phone": "018234324",
        "location": "Naogaon",
        "socials": [
            {
                "name": "Facebook",
                "url": "https://www.facebook.com/shakil"
            }, {
                "name": "Github",
                "url": "https://www.github.com/shakil"
            }
        ]
    }
]

object_json = json.dumps(my_objects, indent=3)
json_file = open("./datas/data.json", "w")
json_file.write(object_json)
json_file.close()

if __name__ == '__main__':
    print(object_json)