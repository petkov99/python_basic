target = int(input())

earned_money = 0
flag = False
while True:
    service = input()
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

    if service == 'closed':
        break

if earned_money < target:
    diff = abs(target - earned_money)
    print(f'Target not reached! You need {diff}lv. more.')
    print(f'Earned money: {earned_money}lv.')

if earned_money > target:
    flag = True
    print('You have reached your target for the day!')
    print(f'Earned money: {earned_money}lv.')





