def fibonacci(n):
    if not (isinstance(n, int) and n >= 0):
        return False
    
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n -2)

print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(2))