name = input('Enter a customer name: ')
print()
with open('transactions.txt') as file_object:
    transactions = file_object.readlines()

lst = []
for transaction in transactions:
    lst.append(transaction.split('|'))

new_lst = []

for item in lst:
    if name in item:
        date_amount = item[0], float(item[2])
        new_lst.append(date_amount)

totals = []
print(f'Transactions with customer {name}:\nDate\t\tAmount')
for thing in new_lst:
    print(f'{thing[0]}\t{round(thing[1], 2)}')
    totals.append(thing[1])

print()
total = sum(totals)
if total >= 0:
    print(f'In total, {name} paid us {total}')
else:
    print(f'In total, we have paid {name} {round(abs(total), 2)}')