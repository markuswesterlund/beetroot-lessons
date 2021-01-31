import json

with open("pb.json") as file_object:
    pb = json.load(file_object)

for k, v in pb.items():
    print(k, ":", v)