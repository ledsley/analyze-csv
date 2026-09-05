import csv

with open('cars_dataset.csv','r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    columns_dict = next(csv_reader)
    
    columns_set = set(columns_dict)
    
print(columns_set)

print(columns_dict)