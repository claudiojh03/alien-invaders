filename = input('file: ')

with open(filename) as file_object:
    lst = file_object.readlines()


names = str(lst)
print(names)
customers = names.split
print(customers)

output = input('output file: ')

with open(output, 'w') as file_object2:
    file_object2.write(str(names))
    print('done')