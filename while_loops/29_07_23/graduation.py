student_name = input()
count_years = 0
fails_count = 0
all_grades = 0

while True:
    annual_grades = float(input())

    if annual_grades < 4.00:
        fails_count += 1

        if fails_count > 1:
            current_year = count_years + 1
            print(f"{student_name} has been excluded at {current_year} grade")
            break

        continue

    else:
        all_grades += annual_grades
        count_years += 1

    if count_years == 12:
        average_grade = all_grades / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break
