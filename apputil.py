import seaborn as sns
import pandas as pd


# Exercise 1
# create a pandas Series of Fibonacci numbers up to n
def fib_series(n):
    values = [fib(i) for i in range(n+1)]
    return pd.Series(values, index=range(n+1), name="Fibonacci")

