needed_money = float(input())
own_money = float(input())

day_count = 0
spend_days = 0
total_sum = own_money
while total_sum < needed_money:
    if spend_days == 5:
        break

    action = input()
    amount = float(input())

    day_count += 1

    if action == 'spend':
        total_sum -= amount
        spend_days += 1
        if total_sum < 0:
            total_sum = 0
    else:
        spend_days = 0
        total_sum += amount

if spend_days == 5:
    print("You can't save the money.")
    print(f"{day_count}")

else:
    print(f"You saved the money for {day_count} days.")
