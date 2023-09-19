annual_tax_for_basketball_training = int(input())

price_for_training = annual_tax_for_basketball_training
price_for_basketball_shoes = annual_tax_for_basketball_training - annual_tax_for_basketball_training * 0.4
price_for_basketball_equipment = price_for_basketball_shoes - price_for_basketball_shoes * 0.2
price_for_ball = (1/4) * price_for_basketball_equipment
price_for_accessories = (1/5) * price_for_ball
total_price = price_for_training + price_for_basketball_shoes \
              + price_for_basketball_equipment + price_for_ball + price_for_accessories

print(total_price)