deposit_money = float(input())
deposit_time_in_months = int(input())
annual_interest_rate = float(input())

per_year = deposit_money * (annual_interest_rate / 100)
per_one_month = per_year / 12
total_sum = deposit_money + deposit_time_in_months * per_one_month

print(total_sum)




