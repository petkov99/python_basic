current_hour = int(input())
current_day = input()

if current_day == 'Monday' or current_day == 'Tuesday' or current_day == 'Wednesday' or current_day == 'Thursday' or \
        current_day == 'Friday' or current_day == 'Saturday':
    if 10 <= current_hour <= 18:
        print('open')
    else:
        print('closed')
else:
    print('closed')
