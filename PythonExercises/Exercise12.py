print("Exercise 12 \n")

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print("5th Fibonacci Number:", fib(5))
print("10th Fibonacci Number:", fib(10))
print("15th Fibonacci Number:",fib(15))
print("20th Fibonacci Number:", fib(20))