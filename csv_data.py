import csv

from collections import defaultdict

with open('cars_dataset.csv','r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    columns_list = next(csv_reader)
    
    columns_set = set(columns_list)
    
#print(columns_set)

#print(columns_list)

with open('cars_dataset.csv','r', encoding='utf-8-sig') as file:
    #reader = csv.DictReader(file)
    
    columns_l = [*csv.DictReader(file)]

columns_dict = defaultdict(list)
for d in columns_l:
    for k,v in d.items():
        columns_dict[k].append(v)

columns_dict = dict(columns_dict)    
#print(columns_dict) # списки значений в choices