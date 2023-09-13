import json

filename = "tm.json"

data = open(filename, 'r')
tm = json.load(data)

print(data)

print(tm)
print(tm["q0"])
print(tm["F"])

q = "q2"
print(tm["Delta"][q])
print(q in tm["F"])
