width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
box_sum = 0
input_line = input()

while input_line != 'Done':
    boxes = int(input_line)
    box_sum += boxes

    if box_sum >= volume:
        break

    input_line = input()

diff = abs(volume - box_sum)
if box_sum > volume:
    print(f"No more free space! You need {diff} Cubic meters more.")

else:
    print(f"{diff} Cubic meters left.")


