scores = [4, 6, 8, 10, 12, 14, 16, 582]
scores.sort
if len(scores) % 2 != 0:
    print(scores[len(scores)//2])
else:
    avg = (scores[(len(scores)//2)-1] + scores[(len(scores)//2)])/2
    print(avg)

#part 2

input_file = 'transactions.txt'
with open(input_file) as file_object:
    lines = file_object.readlines()
    for line in lines: 
        split_line = line.split('|')
        if float(split_line[2]) > 0:
            print(f'{split_line[1]} paid us on {split_line[0]}')
        else:
            print(f'we paid {split_line[1]} on {split_line[0]}')