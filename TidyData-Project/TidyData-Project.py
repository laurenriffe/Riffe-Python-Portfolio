import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset with error handling
file_path = "olympics_08_medalists (1).csv"
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
    exit()

# Initial Data Inspection
print("Initial Data Preview:")
print(df.head())
print("\nData Information:")
print(df.info())

# Reshape the dataset using melt()
df_melted = df.melt(id_vars=["medalist_name"], var_name="event", value_name="medal")

# Drop missing values
df_melted = df_melted.dropna().reset_index(drop=True)

# Extract 'gender' and 'sport' from 'event'
df_melted[['gender', 'sport']] = df_melted['event'].str.split('_', n=1, expand=True)

# Clean 'sport' column
df_melted['sport'] = df_melted['sport'].str.replace('_', ' ')

# Drop original 'event' column
df_melted = df_melted.drop(columns=['event'])

# Display cleaned data
print("Cleaned Data Preview:")
print(df_melted.head())

# Visualization 1: Medal count by sport
plt.figure(figsize=(12, 6))
sns.countplot(data=df_melted, y='sport', order=df_melted['sport'].value_counts().index, palette="coolwarm")
plt.xlabel("Number of Medals")
plt.ylabel("Sport")
plt.title("Medal Distribution by Sport")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Visualization 2: Medal count by gender
plt.figure(figsize=(8, 5))
sns.countplot(data=df_melted, x='gender', hue='medal', palette="pastel")
plt.xlabel("Gender")
plt.ylabel("Number of Medals")
plt.title("Medal Distribution by Gender")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Pivot table: Count of medals per sport
df_pivot = df_melted.pivot_table(index='sport', columns='medal', aggfunc='size', fill_value=0)
print("Pivot Table:")
print(df_pivot.head())

# Save cleaned dataset
df_melted.to_csv("cleaned_olympics_medalists.csv", index=False)

print("Data cleaning and visualization complete. Cleaned dataset saved.")