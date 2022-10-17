import json
dict1 = {'one':1, 'two':2, 'three': {'three.1': 3.1, 'three.2': 3.2 }}


input = json.dumps(dict1)
my_dict = json.loads(input)
print(my_dict)

