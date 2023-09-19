from math import floor

record_in_seconds = float(input())
distance_meters = float(input())
seconds_swim_one_meter = float(input())

sum_seconds = distance_meters * seconds_swim_one_meter
add_time = floor(distance_meters / 15) * 12.5
sum_time = sum_seconds + add_time
diff = sum_time - record_in_seconds
if record_in_seconds <= sum_time:
    diff = sum_time - record_in_seconds
    print(f"No, he failed! He was{diff: .2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is{sum_time: .2f} seconds.")
    