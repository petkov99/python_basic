
rent = int(input())

price_for_statue = rent - (rent * 0.3)
price_for_catering = price_for_statue - (price_for_statue * 0.15)
price_for_sounding = price_for_catering * 0.5
final_price = rent + price_for_sounding + price_for_statue + price_for_catering

print(f"{final_price: .2f}")

