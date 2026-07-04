"""
========================================================================
PROJECT: E-Commerce Sales Performance Analysis (Python)
DATASET: Amazon Sale Report
TOOLS USED: Python (Pandas, Matplotlib, Seaborn)
DESCRIPTION: This script loads the raw data, cleans it, and generates 
             visualizations for sales by category, top states, and order status.
========================================================================
"""

# ------------------------------------------------------------------------
# STEP 1: Importing Libraries and Loading Data
# ------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading data...")
# Loading the dataset (low_memory=False prevents warnings for large files)
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

# Cleaning: Dropping rows where 'Amount' is missing (NaN)
df = df.dropna(subset=['Amount'])


# ------------------------------------------------------------------------
# STEP 2: Graph 1 - Top Selling Categories
# OBJECTIVE: Visualizing which product categories generate the most revenue.
# ------------------------------------------------------------------------
print("Generating Category graph...")
plt.figure(figsize=(10, 6))
# Calculating total sales per category and sorting them
category_sales = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)

# Creating a Bar Chart
sns.barplot(x=category_sales.index, y=category_sales.values, palette='viridis')
plt.title('Total Sales Revenue by Product Category', fontsize=14)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales (INR)', fontsize=12)
plt.xticks(rotation=45) # Tilting text so it doesn't overlap
plt.tight_layout()

# Saving the graph as an image
plt.savefig('Category_Sales.png')
plt.show()


# ------------------------------------------------------------------------
# STEP 3: Graph 2 - Top 5 States by Order Count
# OBJECTIVE: Visualizing the geographic regions with the highest demand.
# ------------------------------------------------------------------------
print("Generating Top States graph...")
plt.figure(figsize=(10, 6))
# Getting top 5 states
top_states = df['ship-state'].value_counts().head(5)

# Creating a Bar Chart
sns.barplot(x=top_states.index, y=top_states.values, palette='magma')
plt.title('Top 5 States with Highest Order Demand', fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.tight_layout()

# Saving the graph as an image
plt.savefig('Top_5_States.png')
plt.show()


# ------------------------------------------------------------------------
# STEP 4: Graph 3 - Order Status Distribution
# OBJECTIVE: Showing the proportion of Shipped, Cancelled, and Returned orders.
# ------------------------------------------------------------------------
print("Generating Order Status graph...")
plt.figure(figsize=(10, 6))
# Counting order statuses
status_counts = df['Status'].value_counts().head(5) # Taking top 5 statuses for clarity

# Creating a Pie Chart
plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Order Status Distribution (Top 5)', fontsize=14)
plt.axis('equal') # Ensures pie is drawn as a circle
plt.tight_layout()

# Saving the graph as an image
plt.savefig('Order_Status_PieChart.png')
plt.show()

print("All graphs have been generated and saved successfully!")