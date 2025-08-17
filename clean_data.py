import pandas as pd

# 1. Load the dataset
df = pd.read_excel("data/raw_sales.xlsx")

# 2. Basic cleaning
# Remove duplicates
df = df.drop_duplicates()

# Fill missing values (e.g., fill NA in 'Sales' with 0)
df['Sales'] = df['Sales'].fillna(0)

# Convert columns to correct data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 3. Generate a summary report
summary = {
    "Total Sales": df['Sales'].sum(),
    "Average Sales": df['Sales'].mean(),
    "Number of Records": len(df)
}

# Print summary
print("Summary Report:")
for k, v in summary.items():
    print(f"{k}: {v}")

# 4. Save cleaned data
df.to_excel("data/cleaned_sales.xlsx", index=False)
print("\nCleaned data saved to data/cleaned_sales.xlsx")
