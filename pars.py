import argparse

from csv_read import show_column,filter

from csv_data import columns_set,columns_list,columns_dict

parser = argparse.ArgumentParser(prog= 'CSV_Analyze')
parser.add_argument("--column", type=str, help='Введите название колонки')
parser.add_argument("--filter", type= str, help= 'Ввдеите Параметр фильтра')
parser.print_help()

args = parser.parse_args()

if args.column:
    if args.column in columns_dict:
        i = args.column
        show_column(i)
    else : print('колонки не существует')

if args.filter:
    filter(args.filter)
