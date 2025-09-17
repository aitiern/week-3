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

# Exercise 3
# Read data
df_bellevue = pd.read_csv("bellevue.csv")

# Part 1
def task_1():
    global df_bellevue

    # Clean gender column
    if "gender" in df_bellevue.columns:
        df_bellevue["gender"] = df_bellevue["gender"].str.strip().str.lower()
        df_bellevue["gender"] = df_bellevue["gender"].replace({
            "m": "male", "f": "female", "": None, "?": None
        })

    # Count missing values per column
    missing_counts = df_bellevue.isnull().sum()

    # Sort by least → most missing
    sorted_cols = missing_counts.sort_values().index.tolist()
    return sorted_cols

# Part 2
def task_2():
    global df_bellevue

    if "year" not in df_bellevue.columns:
        print("Issue: no 'year' column found.")
        return None

    admissions = df_bellevue.groupby("year").size().reset_index(name="total_admissions")
    return admissions

# Part 3
def task_3():
    global df_bellevue

    if "gender" not in df_bellevue.columns or "age" not in df_bellevue.columns:
        print("Issue: missing 'gender' or 'age' column.")
        return None

    avg_age = df_bellevue.groupby("gender")["age"].mean()
    return avg_age

# Part 4
def task_4():
    global df_bellevue

    if "profession" not in df_bellevue.columns:
        print("Issue: no 'profession' column found.")
        return None

    # Normalize text
    df_bellevue["profession"] = df_bellevue["profession"].str.strip().str.lower()

    # Drop missing values
    profession_counts = df_bellevue["profession"].dropna().value_counts()

    return profession_counts.head(5).index.tolist()
