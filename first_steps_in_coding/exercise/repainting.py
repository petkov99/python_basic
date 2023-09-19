protective_nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hour_for_work = int(input())

price_for_nylon = (protective_nylon + 2) * 1.5
price_for_paint = (paint + paint * 0.1) * 14.5
price_for_paint_thinner = paint_thinner * 5.0
price_for_bags = 0.4
price_for_materials = price_for_bags + price_for_paint + price_for_paint_thinner + price_for_nylon
price_for_workers_per_hour = (price_for_materials * 0.3) * hour_for_work

total_price = price_for_workers_per_hour + price_for_materials

print(total_price)
