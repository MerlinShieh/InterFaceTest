import json
a = r"D:/data/Project/Python/InterFaceTest/utils/readYaml.py"
print(type(a))
print(a)

b = json.loads(json.dumps(eval(a)))
print(b)
print(type(b))
print(json.dumps(b))