import csv
import json

csvfile = open('SortedListOfFile.csv', 'r')
jsonfile = open('file.json', 'w')


reader = csv.DictReader(csvfile)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(', \n')
