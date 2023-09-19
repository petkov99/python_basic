interval_start = int(input())
final_interval = int(input())
magic_number = int(input())

flag = False
combination_count = 0
for x in range(interval_start, final_interval + 1):
    for y in range(interval_start, final_interval + 1):
        combination = x + y
        combination_count += 1
        if combination == magic_number:
            print(f"Combination N:{combination_count} ({x} + {y} = {magic_number})")
            flag = True
            break
    if flag:
        break
else:
    print(f"{combination_count} combinations - neither equals {magic_number}")
