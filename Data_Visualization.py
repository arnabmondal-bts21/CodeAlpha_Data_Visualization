import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

# Basic information
print("Dataset Shape:", df.shape)
print(df.head())
print(df.info())

# Set visual style
sns.set_style("whitegrid")

# 1. Sales by Category
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Category", y="Sales", estimator=sum, errorbar=None)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# 2. Profit by Category
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Category", y="Profit", estimator=sum, errorbar=None)
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# 3. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=region_sales, x="Region", y="Sales")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# 4. Profit by Region
region_profit = df.groupby("Region")["Profit"].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=region_profit, x="Region", y="Profit")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.show()

# 5. Sales by Sub-Category
subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=subcategory_sales,
    x="Sales",
    y="Sub-Category"
)
plt.title("Total Sales by Sub-Category")
plt.xlabel("Total Sales")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("sales_by_subcategory.png")
plt.show()

# 6. Sales vs Profit
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category")
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("sales_vs_profit.png")
plt.show()

# 7. Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], bins=30, kde=True)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

print("\nData visualization project completed successfully!")
