list1 = ['this', 'is', 'a', 'list', 'that', 'is', 'supposed', 'to', 'have', 'things']

list3 = list1[:]

list1 = [word.upper() for word in list1]
list2 = list1
list3 = list1[:]
print(list1)
print(list2)

list3 = [wrd.title() for wrd in list3]
print(list3)

# you can't modify the elements of a tuple

tuple1 = tuple([list_element for list_element in list3])
print(tuple1)
print(type(tuple1))

#the solution I found was to use list comprehension and turn that into a tuple and assign it a name. I used the type command to make sure it was a tuple

debtor1 = ('John', 13,)
debtor2 = ('Ian', 70,)
debtor3 = ('Maggie', 55,)
debtor4 = ('Nikolai', 100,)
debtor5 = ('Samantha', 42,)

list_debtors = [debtor1, debtor2, debtor3, debtor4, debtor5]

for debtor in list_debtors:
    print(f"Friends Name:", debtor[0], 'Amount Owed:', debtor [1])

for debtor in list_debtors:
    total = sum(debtor[1])
    print(total)