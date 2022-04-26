my_list = ['this', 'is', 'a', 'string']
my_list = [word.upper() for word in my_list]
print(my_list)

length = int(input('range of x values:'  ))
base = 2
x_vals = list(range(0, length))
y_vals = [base**x for x in x_vals]
print(y_vals)
print(sum(y_vals))

sum = 0
for p in y_vals:
    sum = sum + p

print(sum)