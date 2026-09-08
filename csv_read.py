import csv
from csv_data import columns_dict

def show_column(i):
        print(columns_dict[i])
            
def filter_price(s):
    i_price = []
    if s[0] == '<':
        if s[1] == '=':
            
            value = int(s[2:])
            
            for i,r in enumerate(columns_dict['price_rub']):
                if int(r) <= value:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_price.append(i)
            
        else:
            
            value = int(s[1:])
            
            for i,r in enumerate(columns_dict['price_rub']):
                if int(r) < value:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_price.append(i)
                    
    if s[0] == '>':
        if s[1] == '=':
            value = int(s[2:])
            
            for i,r in enumerate(columns_dict['price_rub']):
                if int(r) >= value:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_price.append(i)
            
        else: 
            value = int(s[1:])
            
            for i,r in enumerate(columns_dict['price_rub']):
                if int(r) > value:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_price.append(i)
                    
    if s[0] == '=':
        
        if s[1] == '=':value = int(s[2:])
            
        else:value = int(s[1:])

        for i,r in enumerate(columns_dict['price_rub']):
            if int(r) == value:
                #print([columns_dict[k][i] for k in columns_dict])
                i_price.append(i)
                    
                    
    if s[0].isdigit():
        value = int(s)
        for i,r in enumerate(columns_dict['price_rub']):
            if int(r) == value:
                #print([columns_dict[k][i] for k in columns_dict])
                i_price.append(i)
                
    return i_price
                    
def filter_year(s):
    i_year = []
    if s[0] == '>':
        if s[1] == '=':
            v = int(s[2:])
            
            for i,r in enumerate(columns_dict['year']):
                        if int(r) >= v:
                            #print([columns_dict[k][i] for k in columns_dict])
                            i_year.append(i)
                        
        else: 
            v = int(s[1:])
            for i,r in enumerate(columns_dict['year']):
                if int(r) > v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_year.append(i)
                    
    if s[0] == '<':
        if s[1] == '=':
            v = int(s[2:])
            
            for i,r in enumerate(columns_dict['year']):
                if int(r) <= v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_year.append(i)
            
        else:
            v = int(s[1:])
            for i,r in enumerate(columns_dict['year']):
                if int(r) < v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_year.append(i)
                    
    if s[0] == '=':
        if s[1] == '=':v = int(s[2:])
            
        else: v = int(s[1:])
            
        for i,r in enumerate(columns_dict['year']):
            if int(r) == v:
                #print([columns_dict[k][i] for k in columns_dict])
                i_year.append(i)
                
    if s[0].isdigit():
        v = int(s)
        
        for i,r in enumerate(columns_dict['year']):
            if int(r) == v:
                #print([columns_dict[k][i] for k in columns_dict])
                i_year.append(i)
                
    return i_year
                
def filter_mileage(s):
    i_mileage = []
    if s[0] == '>':
        if s[1] == '=':
            v = int(s[2:])
            for i,r in enumerate(columns_dict['mileage_km']):
                if int(r) >= v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_mileage.append(i)
            
        else:
            v = int(s[1:])
            
            for i,r in enumerate(columns_dict['mileage_km']):
                if int(r) > v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_mileage.append(i)
                    
    if s[0] == '<':
        if s[1] == '=':
            v = int(s[2:])
            
            for i,r in enumerate(columns_dict['mileage_km']):
                if int(r) <= v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_mileage.append(i)
            
        else:
            v = int(s[1:])
            
            for i,r in enumerate(columns_dict['mileage_km']):
                if int(r) < v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_mileage.append(i)
                    
    if s[0] == '=':
        if s[1] == '=': v = int(s[2:])
            
        else: v = int(s[1:])
        
        for i,r in enumerate(columns_dict['mileage_km']):
            if int(r) == v:
                #print([columns_dict[k][i] for k in columns_dict])
                i_mileage.append(i)
                
    if s[0].isdigit():
        v = int(s)
        
        for i,r in enumerate(columns_dict['mileage_km']):
            if int(r) == v:
                #print([columns_dict[k][i] for k in columns_dict])
                i_mileage.append(i)
    
    return i_mileage
                
def filter_eng(s):
    i_engine = []
    if s[0] == '>':
        if s[1] == '=':
            v = float(s[2:])
            
            for i,r in enumerate(columns_dict['engine_l']):
                if float(r) >= v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_engine.append(i)
            
        else:
            v = float(s[1:])
            
            for i,r in enumerate(columns_dict['engine_l']):
                if float(r) > v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_engine.append(i)
    
    if s[0] == '<':
        if s[1] == '=':
            v = float(s[2:])
            for i,r in enumerate(columns_dict['engine_l']):
                if float(r) <= v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_engine.append(i)
            
        else: 
            v = float(s[1:])
            for i,r in enumerate(columns_dict['engine_l']):
                if float(r) < v:
                    #print([columns_dict[k][i] for k in columns_dict])
                    i_engine.append(i)
                    
    if s[0] == '=':
        if s[1] == '=':v = float(s[2:])
            
        else: v =float(s[1:])
        
        for i,r in enumerate(columns_dict['engine_l']):
            if float(r) == v:
                #print([columns_dict[k][i] for k in columns_dict])
                i_engine.append(i)
                
    if s[0].isdigit():
        v = float(s)
        for i,r in enumerate(columns_dict['engine_l']):
            if float(r) == s:
                #print([columns_dict[k][i] for k in columns_dict])
                i_engine.append(i)
                
    return i_engine
                      
#переделать функции в одну общую подавая в нее 2 значения( строка, ключ) #filter_price(args.price, 'price_rub') мб так\
    
def filter_str_args(s, column_name):
    indexes = []
    for i,r in enumerate(columns_dict[column_name]):
        if r == s:
            indexes.append(i)
    print(len(indexes)) 
    return indexes