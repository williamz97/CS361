print("Exercise 3 \n")

print("(a)", float(123))
print("(b)", float('123'))
print("(c)", float('123.23'))
print("(d)", int(123.23))
try:
    print("(e)", int('123.23'))
except ValueError:
    print("(e) Value Error, passing a float as string to be cast to int")
print("(f)", int(float('123.23')))
print("(g)", str(12))
print("(h)", str(12.2))
print("(i)", bool('a'))
print("(j)", bool(0))
print("(k)", bool(0.1))



