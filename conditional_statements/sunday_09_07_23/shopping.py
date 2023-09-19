budget = float(input())
count_video = int(input())
count_processors = int(input())
count_ram = int(input())

price_for_video = count_video * 250
price_for_processors = count_processors * (price_for_video * 0.35)
price_for_ram = count_ram * (price_for_video * 0.1)

total_sum = price_for_ram + price_for_processors + price_for_video

if count_video > count_processors:
    total_sum = total_sum * 0.85

diff = abs(total_sum - budget)
if budget >= total_sum:
    print(f"You have{diff: .2f} leva left!")
else:
    print(f'Not enough money! You need{diff: .2f} leva more!')

