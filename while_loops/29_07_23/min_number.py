from sys import maxsize

max_num = maxsize

while True:
    user_input = input()
    if user_input == "Stop":
        break

    data = int(user_input)

    if data <= max_num:
        max_num = data
        continue

print(max_num)
