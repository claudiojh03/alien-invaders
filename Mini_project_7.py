def dict_maker(file):
    with open(file) as customers_object:
        list = customers_object.readlines()
        
        new_list = []
        for x in list:
            new_list.append(x.strip())
        
        lst3 = []
        for x in new_list:
            lst3.append(x.split(','))

        lst4 = []
        for date, name, department, time in lst3:
            dict_customer = {'date': date, 'cust': name, 'dept': department, 'time': time}
            lst4.append(dict_customer)
        return lst4
        

def custs_date(dict_maker, date):
    lst5 = []
    for idx in range(len(dict_maker)):
        if dict_maker[idx]['date'] == date and dict_maker[idx]['cust'] not in lst5:
            lst5.append(dict_maker[idx]['cust'])
    return lst5

def time_tracker(dict_maker, name, date):
    lst6 = []
    for idx in range(len(dict_maker)):
        if dict_maker[idx]['cust'] == name and dict_maker[idx]['date'] == date:
            lst6.append(dict_maker[idx])
    dict1 = {}
    for dict in lst6:
        if dict['dept'] not in dict1:
            dict1[dict['dept']] = dict['time']
        elif dict['dept'] in dict1:
            dict1[dict['dept']] = float(dict1.get(dict['dept'])) + float(dict.get('time'))
    return dict1

filename = (input('filename: '))
date = input('date: ')
print(custs_date(dict_maker(filename), date))

dict2 = {}
for customer in custs_date(dict_maker(filename), date):
    dict2[customer] = max(time_tracker(dict_maker(filename), customer, date))
print(dict2)
