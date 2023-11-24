import json

person={"name":"toledo","age":55,"country":"Ghana"}
dom=json.dumps(person)
print(dom["name"])