import json
from person_model import Person


def read_file(file_name):
    with open(file_name) as file:
        return json.load(file)


prabhu_data = read_file("example/prabhu.json")
anupam_data = read_file("example/anupam.json")
properties_prabhu = Person.parse_obj(prabhu_data)
properties_anupam = Person.parse_obj(anupam_data)
result = properties_prabhu == properties_anupam
print(result)
