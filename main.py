import pandas as pd

# Load the Titanic dataset from a public URL
dataset_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(dataset_url)

# Display the first five records
print("--- First 5 Records ---")
print(df.head())

# Display the last five records
print("\n--- Last 5 Records ---")
print(df.tail())
