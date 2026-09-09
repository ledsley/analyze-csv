from csv_data import columns_dict
import operator

def show_column(i):
        print(columns_dict[i])

def filter_num_args_new(s,column_name,value_type):
    indexes = []
    op = []
    value=[]
    for i,elem in enumerate(s):
        if not s[i].isdigit():
            op = s[:i+1]
        else: 
            value = s[i:]
            break
        
    value = value_type(value)
    
    ops ={
        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '=': operator.eq,
        '==': operator.eq,
        '': operator.eq
    }
    
    for i,r in enumerate(columns_dict[column_name]):
        if ops[op](value_type(r),value) == True:
            print([columns_dict[k][i] for k in columns_dict])
            indexes.append(i)
    
    return indexes
                      
#переделать функции в одну общую подавая в нее 2 значения( строка, ключ) #filter_price(args.price, 'price_rub') мб так\
    
def filter_str_args(s, column_name):
    indexes = []
    for i,r in enumerate(columns_dict[column_name]):
        if r == s:
            indexes.append(i)
    print(len(indexes)) 
    return indexes