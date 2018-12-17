print("Exercise 13: \n")

import re

file = open('email.txt', 'r')
file = file.read()

email = re.findall(r'([^ ]+[@][^ ]+[.][a-z]+)', file)
print(email)
