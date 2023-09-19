
film_budget = float(input())
number_of_statists = int(input())
cloths_for_one_statist = float(input())
left_money = 0
needed_money = 0
final_money_for_film = 0
money_for_cloths = 0

money_for_decorations = film_budget * 0.1
# if number_of_statists < 150:
#     money_for_cloths = number_of_statists * cloths_for_one_statist
#     final_money_for_film = money_for_cloths + money_for_decorations
#     left_money = film_budget - final_money_for_film
#
# if film_budget > final_money_for_film:
#     print("Action!")
#     print("Wingard starts filming with" + f"{left_money: .2f}" + " leva left.")

if number_of_statists > 150:
    money_for_cloths = number_of_statists * cloths_for_one_statist - (money_for_cloths * 0.1)
    final_money_for_film = money_for_cloths + money_for_decorations
    left_money = film_budget - final_money_for_film







