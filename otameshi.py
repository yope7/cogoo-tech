# function for calculating fibonacci using iteration
# by GitHub Copilot

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, b+a
    return a

print(fib(25))

