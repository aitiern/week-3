import seaborn as sns
import pandas as pd


# Exercise 1
# create a pandas Series of Fibonacci numbers up to n
def fib_series(n):
    values = [fib(i) for i in range(n+1)]
    return pd.Series(values, index=range(n+1), name="Fibonacci")

# Exercise 2

def to_binary(n):
    # Base case: 0 and 1
    if n < 2:
        return str(n)
    else:
        # Recursive case: divide by 2, then append remainder
        return to_binary(n // 2) + str(n % 2)
