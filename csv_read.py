import csv
from csv_data import columns_dict

#with open('cars_dataset.csv', 'r', newline='') as csv_file:
#    csv_reader = csv.reader(csv_file)
    
def show_column(i):
        print(columns_dict[i])
            
def filter_def(value):
    with open('cars_dataset.csv','r', newline='') as  file:    #переделать функцию чтобы убрать отркытие файла
        reader = csv.reader(file)
        k=0
        for row in reader:
           s_row = set(row)
           if value in s_row:
               k+=1
               print(row)
        if k ==0:
            print('По заданному фильтру ничего не нашлось')
            
def filter_price(s):
    
    indexes = []
    
    if s[0] == '<':
        if s[1] == '=':
            
            value = int(s[2:])
            
            for r in columns_dict['price_rub']:
                if int(r) <= value:
                    i = columns_dict['price_rub'].index(r)
                    print([columns_dict[k][i] for k in columns_dict])
            
        else:
            
            value = int(s[1:])
            
            for r in columns_dict['price_rub']:
                if int(r) < value:
                    i = columns_dict['price_rub'].index(r)
                    print([columns_dict[k][i] for k in columns_dict])  # повторить для остальных операторов
          