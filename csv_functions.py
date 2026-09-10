from csv_data import columns_dict
import operator
from collections import defaultdict

def show_column(i):
        print(columns_dict[i])

def filter_num_args(s,column_name,value_type):
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
            indexes.append(i)
    
    return indexes
    
def filter_str_args(s, column_name):
    indexes = []
    for i,r in enumerate(columns_dict[column_name]):
        if r == s:
            indexes.append(i) 
    return indexes

def stats_c(s):
    if '.' in s[0]:
        data_type = float
    else: data_type = int
    
    s = [data_type(x) for x in s]
    n = len(s)
    print(f'количество:{n}')
    print(f'максимум:{max(s)}')
    print(f'минимум:{min(s)}')
    print(f'срденее значение:{round(sum(s)/n,1)}')
    
def grouping(column_name):
    s = list(set(columns_dict[column_name]))
    indexes = []
    for j in range(len(s)):
        in_j = []
        for i,r in enumerate(columns_dict[column_name]):
            if s[j] == r:
                in_j.append(i)
        indexes.append(in_j)
    return s,indexes

def grouping(column_name):
   s =defaultdict(list)
   for i,r in enumerate(columns_dict[column_name]):
       s[r].append(i)
       
   s = dict(s)
   return s