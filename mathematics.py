#factors are the numbers that can divide a number without a remainder
def factors(number):
    for i in range(1, number + 1):
        if (number % i == 0):
            print(i)

factors(13)            
