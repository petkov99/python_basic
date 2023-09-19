number_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())

time_per_book = number_of_pages // pages_per_hour
time_per_day = time_per_book // days

print(time_per_day)



