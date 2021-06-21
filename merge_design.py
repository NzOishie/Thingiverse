
import json
import os


def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('designs.json', 'w') as output_file:
        json.dump(result, output_file)


path = "designs/"
files = os.listdir(path)
file_list = []
for file in files:
    print(file)
    if file.endswith('.json'):
        file_list.append("designs/"+file)
print((file_list))
files = ["designs/designs-TeamTeamUSA-1.json","designs/designs-adafruit-2.json"]
merge_JsonFiles(file_list)
