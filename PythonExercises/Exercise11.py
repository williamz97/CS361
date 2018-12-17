print("Exercise 11 \n")

def iteration_sum_list(list):
    iterator = 0
    sum = 0

    while iterator < len(list):
        sum += list[iterator]
        iterator += 1
    return sum

def recursive_sum_list(list):
    sum = 0

    if len(list) == 0:
        return sum
    else:
        sum = list[0]
        del list[0]
        return sum + recursive_sum_list(list)

a = [8, 9, 7, 2, 1]
print("Sum of all elements in list a using iteration:", iteration_sum_list(a))
print("Sum of all elements in a list using recursion:", recursive_sum_list(a))