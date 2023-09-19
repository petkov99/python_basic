number = int(input())
sum_all_numbers = 0

while True:
    current_numb = int(input())
    sum_all_numbers += current_numb

    if sum_all_numbers >= number:
        print(sum_all_numbers)
        break

