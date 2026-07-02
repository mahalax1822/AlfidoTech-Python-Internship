import pandas as pd

# Read the CSV file
df = pd.read_csv("students.csv")

print("========== Student Records ==========\n")
print(df)

# Calculate average marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("\n========== Average Marks ==========\n")
print(df[["Name", "Average"]])

# Find topper
topper = df.loc[df["Average"].idxmax()]

print("\n========== Topper ==========")
print("Name:", topper["Name"])
print("Average:", round(topper["Average"], 2))

# Subject averages
print("\n========== Subject Averages ==========")
print("Maths:", round(df["Maths"].mean(), 2))
print("Science:", round(df["Science"].mean(), 2))
print("English:", round(df["English"].mean(), 2))

# Save results
df.to_csv("result.csv", index=False)

print("\nResult saved successfully as result.csv")