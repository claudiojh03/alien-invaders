could_points = int(input('Points you could have scored: '))
scored_points = int(input('Points you scored: '))

points_ratio = scored_points/could_points
points_percent = points_ratio*100

print(f'{points_percent}%')

if points_percent >= 92:
    print('A')
elif points_percent >= 90 and points_percent < 92:
    print('A-')
elif points_percent >= 88 and points_percent < 90:
    print('B+')
elif points_percent >= 82 and points_percent < 88:
    print('B')
elif points_percent >= 80 and points_percent < 82:
    print('B-')
elif points_percent >= 78 and points_percent < 80:
    print('C+')
elif points_percent >= 72 and points_percent < 78:
    print('C')
elif points_percent >= 70 and points_percent < 72:
    print('C-')
elif points_percent >= 68 and points_percent < 70:
    print('D+')
elif points_percent >= 62 and points_percent < 68:
    print('D')
elif points_percent >= 60 and points_percent < 62:
    print('D-')
else:
    print('F')

#Part 2

customer_names = ['Josh', 'Nick', 'Claudio']
name = input('What is your name? ').title()

if name in customer_names:
    print(f'Welcome back {name}!')
else:
    print(f'{name}, please register.')