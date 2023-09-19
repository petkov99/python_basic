def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

upper_bound_first = int(input())
upper_bound_second = int(input())
upper_bound_third = int(input())

valid_pins = []

for first_digit in range(2, upper_bound_first + 1, 2):
    for second_digit in range(2, upper_bound_second + 1):
        if is_prime(second_digit):
            for third_digit in range(2, upper_bound_third + 1, 2):
                valid_pins.append(f"{first_digit} {second_digit} {third_digit}")

print('\n'.join(valid_pins))