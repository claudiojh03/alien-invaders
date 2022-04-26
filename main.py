stocks_filename = input('Stock File Name: ')

with open(stocks_filename) as stocks_object:
    lines = [line.strip().split(',') for line in stocks_object]
    
lst_dict = []
for stock in lines:
    stock_dict = {}
    name_stock, start, finish = stock
    stock_dict['name'] = name_stock
    stock_dict['start'] = start
    stock_dict['finish'] = finish
    lst_dict.append(stock_dict)

dict_dict = {}
for stock in lines:
    stock_dict = {}
    name_stock, start, finish = stock
    stock_dict['start'] = start
    stock_dict['finish'] = finish
    dict_dict[name_stock] = stock_dict

change_price_dict = {}
for stock in lst_dict:
    stock_name = stock.get('name')
    change_price = float(stock['finish']) - float(stock['start'])
    change_price_dict[stock_name] = change_price

max_value = round((max(change_price_dict.values())), 2)
max_key = max(change_price_dict, key=change_price_dict.get)
max_value_percent = round((float(max_value)/100)*(float(dict_dict[max_key]['start'])), 2)

min_value = round((min(change_price_dict.values())), 2)
min_key = min(change_price_dict, key=change_price_dict.get)
min_value_percent = round((float(min_value)/100)*(float(dict_dict[min_key]['start'])), 2)

if max_value > 0:
    print(f'{max_key} went up by {max_value}, which is also {max_value_percent}%')
else:
    print('No stock went up today')

if min_value < 0:
    print(f'{min_key} went down by {min_value}, which is also {min_value_percent}%')
else:
    print('No stock went down today')