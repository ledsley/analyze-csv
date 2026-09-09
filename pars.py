import argparse

from csv_read import show_column, filter_num_args, filter_num_args, filter_str_args

from csv_data import columns_dict

parser = argparse.ArgumentParser(prog= 'CSV_Analyze')
subparsers = parser.add_subparsers(help = 'sub')

parser.add_argument("--column", choices= (columns_dict.keys()), help='Введите название колонки')

sub_filter = subparsers.add_parser('f', help='введите фльтр')
sub_filter.add_argument('--brand',choices=(set(columns_dict.get('brand'))), help='Введите название бренда')
sub_filter.add_argument('--model',choices=(set(columns_dict.get('model'))),help='Введите название модели')
sub_filter.add_argument('--year', type=str, help='Введите год авто')
sub_filter.add_argument('--mileage', type=str, help='Введите пробег')
sub_filter.add_argument('--engine_l', type=str, help='Введите объем двигателя')
sub_filter.add_argument('--fuel', choices=(set(columns_dict.get('fuel'))),help='Введите тип топлива')
sub_filter.add_argument('--transmission', choices=(set(columns_dict.get('transmission'))),help= 'Ввдеите тип кпп')
sub_filter.add_argument('--city', choices=(set(columns_dict.get('city'))), help='Введите город поиска')
sub_filter.add_argument('--price', type=str, help='Введите оператор и цену без пробела')

parser.print_help()

args = parser.parse_args()

if args.column:
    if args.column in columns_dict:
        i = args.column
        show_column(i)
    else : print('колонки не существует')
    
final_indexes = []
 
if args.brand:
    final_indexes.append(filter_str_args(args.brand, 'brand'))
    
if args.model:
    final_indexes.append(filter_str_args(args.model, 'model'))
    
if args.fuel:
    final_indexes.append(filter_str_args(args.fuel,'fuel'))
    
if args.city:
    final_indexes.append(filter_str_args(args.city, 'city'))
    
if args.price:
    final_indexes.append(filter_num_args(args.price,'price_rub',int))
    
if args.year:
    final_indexes.append(filter_num_args(args.year,'year',int))
    
if args.mileage:
    final_indexes.append(filter_num_args(args.mileage,'mileage',int))
    
if args.engine_l:
    final_indexes.append(filter_num_args(args.engine_l,'engine_l',float))
    
if args.transmission:
    final_indexes.append(filter_str_args(args.transmission,'transmission'))

intersection_indexes =final_indexes[0]

n = len(final_indexes)

if n>1:
    for i in range(1,len(final_indexes)):
        set_i = set(final_indexes[i])
        intersection_indexes = [x for x in intersection_indexes if x in set_i]

for i in intersection_indexes:
    print([columns_dict[k][i] for k in columns_dict])