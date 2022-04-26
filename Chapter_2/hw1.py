# Question 1
sentence = 'this is a string that contains whatever I want'
print(sentence.lower())
print(sentence.upper())
print(sentence.title())
# Question 2
print(sentence.swapcase())
# Question 3 "The code in question 3 creates a new variable called 'new_sentence' in which any 'e' in the variable 'sentence' is replaced by '#'."
new_sentence = sentence.replace('e','#')
print(new_sentence)
# Question 4
x = 4.7
y = 5*x**2-2*x+3
print(y)