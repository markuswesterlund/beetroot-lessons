import json

pb = {}
pb["first_name"] = "Markus"
pb["last_name"] = "Westerlund"
pb["full_name"] = "Markus Westerlund"
pb["phone_number"] = "1234567890"
pb["city"] = "Sundsvall"

with open("pb.json", "w") as file_object:
    json.dump(pb, file_object)