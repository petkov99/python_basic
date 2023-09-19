import sys

n = int(input())

sum_num = 0
max_num = -sys.maxsize

for i in range(n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_num += num
if max_num == sum_num - max_num:
    print('Yes')
    print(f'Sum = {sum_num - max_num}')
else:
    print("No")
    sum_num = sum_num - max_num
    print(f"Diff = {abs(max_num - sum_num)}")