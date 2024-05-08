import json
from sys import argv

try:
    file1 = argv[1]
    file2 = argv[2]
    file3 = argv[3]
except IndexError:
    print("Need all 3 arguments with filepath")
    exit(1)
def insertValue(li):
    for test in li:
        try:
            if 'values' in test:
                insertValue(test['values'])
            test['value'] = valDict[test['id']]
        except:
            pass
    return


with open(file1, "r") as f:
    tests = json.load(f)
with open(file2, "r") as f:
    values = json.load(f)

tests = tests['tests']
values = values['values']
valDict = {}

for value in values:
    valDict[value['id']] = value['value']

insertValue(tests)

with open(file3, "w") as f:
    json.dump(tests, f, indent=2)

