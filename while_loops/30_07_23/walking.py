input_line = input()

goal = 10000
total_steps = 0

while input_line != 'Going home':
    steps = int(input_line)
    total_steps += steps

    if total_steps >= goal:
        break

    input_line = input()
if input_line == 'Going home':
    steps_home = int(input())
    total_steps += steps_home

diff = abs(total_steps - goal)

if total_steps >= goal:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')



