print("Exercise 5 \n")

def primeNumber():
    number_found = 0
    x = 11

    while number_found < 20:
        test_5 = (x % 5 == 0)
        test_7 = (x % 7 == 0)
        test_11 = (x % 11 == 0)

        if test_5 != 0  and test_7 != 0 and test_11 != 0:
            print(x)
            number_found += 1

        x += 1


print("The first 20 prime numbers \n")
primeNumber()



