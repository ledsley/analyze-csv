import csv
from csv_data import columns_dict

#with open('cars_dataset.csv', 'r', newline='') as csv_file:
#    csv_reader = csv.reader(csv_file)
    
def show_column(i):
        print(columns_dict[i])
            
def filter(value):
    with open('cars_dataset.csv','r', newline='') as  file:
        reader = csv.reader(file)
        k=0
        for row in reader:
           s_row = set(row)
           if value in s_row:
               k+=1
               print(row)
        if k ==0:
            print('По заданному фильтру ничего не нашлось')