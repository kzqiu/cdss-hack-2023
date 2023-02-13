import csv
import re

data = './data/Raw/wishes.csv'

with open(data, mode='r') as inp:
    reader = csv.reader(inp)        

    with open('./data/Raw/wishes_clean.csv', mode='w') as out:
        for i, line in enumerate(inp):
            out.write(re.sub('\{[^]]*?\}', lambda x: x.group(0).replace(',', ';'), line))

