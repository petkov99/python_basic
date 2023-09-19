groups = int(input())
total_people = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups):
    people_in_group = int(input())
    total_people += people_in_group

    if people_in_group <= 5:
        musala += people_in_group
    elif 5 < people_in_group <= 12:
        monblan += people_in_group
    elif 12 < people_in_group <= 25:
        kilimanjaro += people_in_group
    elif 25 < people_in_group <= 40:
        k2 += people_in_group
    elif 40 < people_in_group:
        everest += people_in_group

musala_percents = musala / total_people * 100
monblan_percent = monblan / total_people * 100
kilimanjaro_percents = kilimanjaro / total_people * 100
k2_percents = k2 / total_people * 100
everest_percents = everest / total_people * 100

print(f'{musala_percents:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimanjaro_percents:.2f}%')
print(f'{k2_percents:.2f}%')
print(f'{everest_percents:.2f}%')