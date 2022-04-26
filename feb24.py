filename = input('Filename: ')

with open(filename) as file_object:
    lst_objects = [line.strip().split(',') for line in file_object.readlines()]
    
print(lst_objects)

lst_dicts = []
for name, x, y in lst_objects:
    points_dict = {name: (int(x), int(y))}
    lst_dicts.append(points_dict)

print(lst_dicts)

#part 3 I have no clue what to do for

lst_num = [3, 4, 7, 2, 8]
min = lst_num[0]
for num in lst_num:
    if num < min:
        min = num

print(min)