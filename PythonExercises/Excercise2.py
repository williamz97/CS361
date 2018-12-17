print("Exercise 2 \n")

try:
    print("(a) 2000.3 ** 200=", 2000.3 ** 200)
except OverflowError:
    print("Causes OverFlowError, the result is too large \n")

print("(b) 1.0 + 1.0 - 1.0=", 1.0 + 1.0 - 1.0)
print("Prints out the exact value of 1.0 + 1.0 - 1.0 \n")

print("(c) 1.0 + 1.0e20 - 1.0e20=", 1.0 + 1.0e20 - 1.0e20)
print("Prints out 0 \n")