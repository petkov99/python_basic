current_day = input()

if current_day == 'Monday' or current_day == 'Tuesday' or current_day == 'Wednesday' or current_day == 'Thursday' \
        or current_day == 'Friday':
    print('Working day')
elif current_day == 'Saturday' or current_day == 'Sunday':
    print('Weekend')
else:
    print('Error')


