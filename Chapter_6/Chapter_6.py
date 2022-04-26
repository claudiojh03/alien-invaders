transaction1 = {'date': '23-02-2022', 'name': 'Nikolai', 'amount': '69.42'}
transaction2 = {'date': '24-02-2022', 'name': 'Fred', 'amount': '93.42'}
transaction3 = {'date': '25-02-2022', 'name': 'Nikolai', 'amount': '12.25'}
transaction4 = {'date': '26-02-2022', 'name': 'Jacob', 'amount': '84.21'}
print(transaction1)

transactions = (transaction1, transaction2, transaction3, transaction4)

for transaction in transactions:
    print(transaction)
