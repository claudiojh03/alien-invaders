words = ['something', 'house', 'car', 'soup', 'boy', 'world', 'calculator', 'video', 'music', 'popcorn']
words.sort()
words.pop()
words.pop(0)
words.pop(len(words)//2)
if 'poop' in words:
    words.remove('poop')
print(words)