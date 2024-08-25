def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
    return fib_series[:n]

n = int(input("Enter the number of terms you want to generate: "))
fib_series = fibonacci(n)
print("Fibonacci Series:", fib_series)