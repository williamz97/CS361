print("Exercise 6 \n")

#-----------Part A-----------
def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i < n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

#-----------Part C-----------
def primes_up_to(n):
    counter = 2
    list_of_primes = []

    while counter <= n:

        if is_prime(counter):
            list_of_primes.append(counter)
        counter += 1

    return(list_of_primes)

#-----------Part D-----------
def first_n_primes(n):
    num_primes = n
    counter = 2
    list_of_primes = []

    while num_primes > 0:

        if is_prime(counter):

            num_primes = num_primes - 1
            list_of_primes.append(counter)

        counter += 1

    return(list_of_primes)

#-----------Tests-----------
print("Check if 230 is prime:", is_prime(230))
print("Prints all primes up to 100:", primes_up_to(100))
print("Prints first 50 primes", first_n_primes(50))