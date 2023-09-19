import math

series_name = str(input())
ep_time = int(input())
break_time = int(input())

launch_time = break_time / 8
rest_time = break_time / 4
left_time = break_time - launch_time - rest_time
diff = abs(left_time - ep_time)
rounded_diff = math.ceil(diff)


if left_time >= ep_time:
    print(f"You have enough time to watch {series_name} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {rounded_diff} more minutes.")
