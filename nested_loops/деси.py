target = int(input())
earned_money = 0

while earned_money < target:
    service = input()

    if service == 'closed':
        break

    if service == 'haircut':
        haircut_type = input()
        if haircut_type == 'mens':
            earned_money += 15
        elif haircut_type == 'ladies':
            earned_money += 20
        elif haircut_type == 'kids':
            earned_money += 10
    elif service == 'color':
        color_type = input()
        if color_type == 'touch up':
            earned_money += 20
        elif color_type == 'full color':
            earned_money += 30

if earned_money >= target:
    print('You have reached your target for the day!')
else:
    diff = target - earned_money
    print(f'Target not reached! You need {diff}lv. more.')
print(f'Earned money: {earned_money}lv.')