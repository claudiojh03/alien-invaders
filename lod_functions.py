def sum_key(data, key):
    lst_values = []
    for dict in data:
        lst_values.append(dict[key])
    return sum(lst_values)

def unique_values(data, key):
    lst_values = []
    for dict in data:
        if key in data:
            pass
        else:
            lst_values.append(dict[key])
    print(lst_values)

unique_values([{'k': 6}, {'k':6}, {'k':3}], 'k')