
budget = float(input())
number_of_nights = int(input())
price_for_one_night = float(input())
additional_expenses = int(input())
final_price = 0
left_money = 0
needed_money = 0

if number_of_nights > 7:
    discount = price_for_one_night * 0.05
    final_price_for_night_one_night = price_for_one_night - discount
    final_price_for_all_nights = final_price_for_night_one_night * number_of_nights
    budget_for_expenses = budget * (additional_expenses / 100)
    final_price = final_price_for_all_nights + budget_for_expenses
    left_money = f"{budget - final_price: .2f}"

if number_of_nights <= 7:
    all_night_price = number_of_nights * price_for_one_night
    expenses_budget = budget * (additional_expenses / 100)
    final_price = all_night_price + expenses_budget
    needed_money = f"{final_price - budget: .2f}"

elif budget < final_price:
    print(needed_money + " leva needed.")







