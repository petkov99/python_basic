count_stay = int(input())
room_type = input()
rating = input()

price = 0

if room_type == 'room for one person':
    price = 18 * (count_stay - 1)

elif room_type == 'apartment':
    price = 25 * (count_stay - 1)
    if count_stay < 10:
        price = price * 0.7
    elif 10 < count_stay < 15:
        price = price * 0.65
    elif count_stay > 15:
        price = price * 0.5

elif room_type == 'president apartment':
    price = 35 * (count_stay - 1)
    if count_stay < 10:
        price = price * 0.9
    elif 10 < count_stay < 15:
        price = price * 0.85
    elif count_stay > 15:
        price = price * 0.8
if rating == 'positive':
    price = price + (price * 0.25)
else:
    price = price - (price * 0.1)

print(f"{price:.2f}")


