trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
truck_count = int(input())

# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.

total_sum = (puzzle_count * 2.60) + (dolls_count * 3) + (teddy_count * 4.10) + (minions_count * 8.20) + (truck_count * 2)
total_count = puzzle_count + dolls_count + teddy_count + minions_count + truck_count

if total_count >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)

diff = abs(total_sum - trip_price)
if total_sum >= trip_price:
    print(f"Yes!{diff: .2f} lv left.")
else:
    print(f"Not enough money!{diff: .2f} lv needed.")


