from math import ceil
from math import floor

number_of_people = int(input())
entry_tax = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

entry_for_all_people = number_of_people * entry_tax
used_sunbeds = ceil(number_of_people * 0.75)
price_for_used_sunbeds = used_sunbeds * sunbed_price
used_umbrellas = ceil(number_of_people * 0.5)
price_for_used_umbrellas = used_umbrellas * umbrella_price

total_price = entry_for_all_people + price_for_used_sunbeds + price_for_used_umbrellas

print(f"{total_price: .2f}" + ' lv.')





