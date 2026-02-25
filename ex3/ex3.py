def divide_numbers(dividend, divisor, /, round_to=2):
    return round(dividend / divisor, round_to)

print(divide_numbers(10, 3))
print(divide_numbers(10, 3, round_to=4))
print(divide_numbers(7, 2))

print(divide_numbers(dividend=10, divisor=3))