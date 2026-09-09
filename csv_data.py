import csv

from collections import defaultdict

with open('cars_dataset.csv','r', encoding='utf-8-sig') as file:
    
    columns_l = [*csv.DictReader(file)]

columns_dict = defaultdict(list)
for d in columns_l:
    for k,v in d.items():
        columns_dict[k].append(v)

columns_dict = dict(columns_dict)    