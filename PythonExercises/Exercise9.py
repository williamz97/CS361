print("Exercise 8 \n")

def sublist_elements(list):
    final_list = []
    iterator = 0

    while iterator < len(list):
        counter = 0
        sublist = list[iterator]

        while counter < len(sublist):
            final_list.append(sublist[counter])
            counter += 1
        iterator += 1

    return(print(final_list))


listA = [[1,3],[3,6]]
sublist_elements(listA)

