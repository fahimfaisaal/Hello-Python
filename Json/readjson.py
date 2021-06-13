import json

json_content: list = []
try:
    file_object = open("./datas/data.json", "r")
    json_content = json.loads(file_object.read())
    print(json_content[0])
except:
    print("have no files")

if __name__ == '__main__':
    print(None)
