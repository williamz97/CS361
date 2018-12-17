print("Exercise 7 \n")

#-----------Part A-----------
def printList(list):
    iterator = 0
    while iterator < len(list):
        print(list[iterator])
        iterator += 1
    print("Finished Print List")

#-----------Part B-----------
def reverseprintList(list):
    iterator = len(list) - 1

    while iterator >= 0:
        print(list[iterator])
        iterator = iterator - 1
    print("Finished Reverse Print")

#-----------Part C-----------
def countElements(list):
    counter = 0;

    while counter < len(list):
        counter = counter + 1
    return print("List Element Count", counter)

#-----------Tests-----------
list = [2,3,5,123,4,1,23]
printList(list)
reverseprintList(list)
countElements(list)