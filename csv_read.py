import csv

#with open('cars_dataset.csv', 'r', newline='') as csv_file:
#    csv_reader = csv.reader(csv_file)


columns_set = {'id','brand','model','year','mileage_km','engine_l','fuel','transmission','city','price_rub'}
    
def show_column(i):
    with open('cars_dataset.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row[i])