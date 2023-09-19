chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

price_for_chicken_menu = chicken_menu * 10.35
price_for_fish_menu = fish_menu * 12.4
price_for_vegan_menu = vegan_menu * 8.15
price_for_all_menus = price_for_fish_menu + price_for_vegan_menu + price_for_chicken_menu
price_for_desert = price_for_all_menus * 0.2
delivery = 2.5

total_order_price = price_for_all_menus + price_for_desert +delivery

print(total_order_price)
