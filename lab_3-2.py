# Ryan Lugo: RJl 3/7/22
total = 1


def factorial(number):
    global total
    if number <= 0:
        return 1
    elif number >= 1:
        total = total * number
        factorial(number - 1)
    return total

print(factorial(0))