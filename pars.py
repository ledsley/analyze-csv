import argparse

from csv_read import show_column, show_enggitr

from csv_data import columns_set,columns_dict

parser = argparse.ArgumentParser(prog= 'CSV_Analyze')
parser.add_argument("--column", type=str, help='Введите название колонки')
parser.print_help()

args = parser.parse_args()

if args.column:
    if args.column in columns_set:
        i = columns_dict.index(args.column)
        show_column(i)
    else : print('колонки не сущ')
    