lily_age = int(input())
dish_washer_price = float(input())
single_toy_price = int(input())

toy_count = 0
money_count = 0
brother_money = 0

for year in range(1, lily_age + 1):
    if year % 2 == 0:
        money_count += int(year / 2) * 10
        brother_money += 1
    else:
        toy_count += 1
money_from_toys = toy_count * single_toy_price
total_money = money_from_toys + money_count - brother_money
diff = abs(total_money - dish_washer_price)
if total_money >= dish_washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
