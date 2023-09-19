acc_balance = 0

while True:
    data = input()

    if data == 'NoMoreMoney':
        break

    current_sum = float(data)

    if current_sum >= 0:
        acc_balance += current_sum
        print(f'Increase: {current_sum:.2f}')

    else:
        print(f'Invalid operation!')
        break

print(f'Total: {acc_balance:.2f}')


