import json
from sys import argv


def insertValue(li):
    for test in li:
        try:
            if 'values' in test:
                insertValue(test['values'])
            test['value'] = valDict[test['id']]
        except:
            pass
    return


with open(argv[1], "r") as f:
    tests = json.load(f)
with open(argv[2], "r") as f:
    values = json.load(f)

tests = tests['tests']
values = values['values']
valDict = {}

for value in values:
    valDict[value['id']] = value['value']

insertValue(tests)

with open("report.json", "w") as f:
    json.dump(tests, f, indent=2)
