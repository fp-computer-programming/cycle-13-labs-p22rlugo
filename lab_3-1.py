# Ryan Lugo: RJL 3/7/22

def r_max(num):
    biggestNumber = 0

    for numbers in num:
        if type(numbers) == list:
            r_max(numbers)
        else:
            if numbers > biggestNumber:
                biggestNumber = numbers
    return biggestNumber

print("Here's the biggest number!:",r_max([1,2,3,[4,5],6]))