tournament_played = int(input())
starting_points = int(input())

tournament_points = 0
number_of_wins = 0

for _ in range(tournament_played):
    current_stage = input()
    if current_stage == 'F':
        tournament_points += 1200
    elif current_stage == 'SF':
        tournament_points += 720
    elif current_stage == 'W':
        tournament_points += 2000
        number_of_wins += 1

average_point = int(tournament_points / tournament_played)
all_points = starting_points + tournament_points
win_percentage = number_of_wins / tournament_played * 100

print(f'Final points: {all_points}')
print(f'Average points: {average_point}')
print(f'{win_percentage:.2f}%')


