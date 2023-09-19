n = int(input())

odd_number = 0
even_number = 0

for i in range (1, n + 1):
    current_number = int(input())

    if i % 2 == 0:
        even_number += current_number
    else:
        odd_number += current_number
if odd_number == even_number:
    print('Yes')
    print(f"Sum = {odd_number}")
else:
    diff_number = abs(odd_number - even_number)
    print('No')
    print(f"Diff = {diff_number}")

