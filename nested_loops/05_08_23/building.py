floors = int(input())
rooms = int(input())

for floor in reversed(range(1, floors + 1)):
    room_type = 'A'if floor % 2 else "O"

    if floor == floors:
        room_type = 'L'

    for room in range(rooms):
        room_name = f'{room_type}{floor}{room}'
        print(room_name, end=' ')

    print()

    