width = int(input())
length = int(input())

all_peaces = width * length

no_more_peaces = False
input_line = input()
while input_line != 'STOP':
    current_peace = int(input_line)
    all_peaces -= current_peace

    if all_peaces <= 0:
        no_more_peaces = True
        break

    input_line = input()

if no_more_peaces:
    print(f'No more cake left! You need {abs(all_peaces)} pieces more.')
else:
    print(f'{all_peaces} pieces are left.')