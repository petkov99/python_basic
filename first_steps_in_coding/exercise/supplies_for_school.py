pack_of_pens = int(input())
pack_of_markers = int(input())
detergent_lt = int(input())
discount = int(input())

price_pens = pack_of_pens * 5.80
price_markers = pack_of_markers * 7.2
price_detergent = detergent_lt * 1.2
price_for_all_materials = price_pens + price_markers + price_detergent
price_with_discount = price_for_all_materials - (price_for_all_materials * discount / 100)

print(price_with_discount)