# %%
# =============================================================================
# Assignment: Pandas and Matplotlib Analysis
# =============================================================================

# --- Import Necessary Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Used for better visual styling
import numpy as np     # Used to create sample data and add a NaN

# %%
# =============================================================================
# (Helper Step) Create a Sample CSV File
# =============================================================================
# This cell creates the 'sales_data.csv' file you'll use for the assignment.
# You only need to run this cell once to create the file.

try:
    data = {
        'Date': pd.to_datetime([
            '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
            '2023-02-01', '2023-02-02', '2023-02-03', '2023-02-04', '2023-02-05',
            '2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05'
        ]),
        'Region': [
            'North', 'North', 'South', 'South', 'West',
            'North', 'South', 'West', 'West', 'North',
            'South', 'West', 'North', 'South', 'West'
        ],
        'Product': [
            'A', 'B', 'A', 'C', 'B',
            'A', 'C', 'B', 'A', 'C',
            'A', 'B', 'C', 'A', 'B'
        ],
        'Sales': [
            150, 200, 100, 300, 250,
            160, 120, 280, 220, 210,
            110, 260, 230, 130, 270
        ],
        'Units Sold': [
            15, 20, 10, 30, 25,
            16, 12, 28, 22, 21,
            11, 26, 23, 13, 27
        ]
    }
    
    # Create DataFrame
    df_sample = pd.DataFrame(data)
    
    # Intentionally add a missing value to demonstrate cleaning
    df_sample.loc[3, 'Sales'] = np.nan
    
    # Save to CSV
    df_sample.to_csv('sales_data.csv', index=False)
    
    print("'sales_data.csv' created successfully.")
    
except Exception as e:
    print(f"Error creating sample file: {e}")

# %%
# =============================================================================
# Task 1: Load and Explore the Dataset
# =============================================================================
print("\n--- Task 1: Load and Explore ---")

# --- Load the dataset (with error handling) ---
file_name = 'sales_data.csv'
try:
    df = pd.read_csv(file_name)
    print(f"Successfully loaded '{file_name}'")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    print("Please make sure the file is in the same directory as the script.")
    # In a real script, you might exit here:
    # exit()
except Exception as e:
    print(f"An error occurred: {e}")

# --- Display the first few rows ---
print("\n--- First 5 Rows (df.head()) ---")
print(df.head())

# --- Explore the structure (data types and missing values) ---
print("\n--- Dataset Info (df.info()) ---")
df.info()

# --- Check for missing values ---
print("\n--- Missing Value Count (df.isnull().sum()) ---")
print(df.isnull().sum())

# --- Clean the dataset ---
# We have one missing value in 'Sales'. Let's fill it with the mean of the column.
mean_sales = df['Sales'].mean()
df['Sales'] = df['Sales'].fillna(mean_sales)

# The 'Date' column was loaded as an 'object' (string). 
# We need to convert it to datetime for time-series plotting.
df['Date'] = pd.to_datetime(df['Date'])

print("\n--- Dataset Info after Cleaning and Type Conversion ---")
df.info()
print("\nMissing values after cleaning:")
print(df.isnull().sum())


# %%
# =============================================================================
# Task 2: Basic Data Analysis
# =============================================================================
print("\n--- Task 2: Basic Data Analysis ---")

# --- Compute basic statistics ---
print("\n--- Descriptive Statistics (df.describe()) ---")
print(df.describe())

# --- Perform groupings ---
# Group by 'Region' and compute the mean 'Sales'
print("\n--- Mean Sales by Region ---")
region_sales_mean = df.groupby('Region')['Sales'].mean().sort_values(ascending=False)
print(region_sales_mean)

# Group by 'Product' and compute the total 'Units Sold'
print("\n--- Total Units Sold by Product ---")
product_units_sum = df.groupby('Product')['Units Sold'].sum().sort_values(ascending=False)
print(product_units_sum)

# --- Identify patterns or interesting findings ---
print("\n--- Initial Findings ---")
print(f"1. The average (mean) sale amount is ${df['Sales'].mean():.2f}.")
print(f"2. The 'West' region has the highest average sales (${region_sales_mean.loc['West']:.2f}).")
print(f"3. Product 'B' is the top-selling product by total units sold ({product_units_sum.loc['B']}).")


# %%
# =============================================================================
# Task 3: Data Visualization
# =============================================================================
print("\n--- Task 3: Data Visualization ---")

# Set the visual style for plots
sns.set_style("whitegrid")

# --- 1. Line Chart: Sales Trend Over Time ---
# Group by date to sum sales for each day
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(daily_sales['Date'], daily_sales['Sales'], marker='o', linestyle='-')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.grid(True)

#To show the plot and save it as a PNG file
plt.savefig('1_sales_over_time.png')
plt.show()

# --- 2. Bar Chart: Average Sales by Region ---
plt.figure(figsize=(8, 6))
# Use the 'region_sales_mean' Series we created in Task 2
region_sales_mean.plot(kind='bar', color=['#4C72B0', '#55A868', '#C44E52'])
plt.title('Average Sales per Region')
plt.xlabel('Region')
plt.ylabel('Average Sales ($)')
plt.xticks(rotation=0)  # Keep the x-axis labels horizontal
plt.savefig('2_avg_sales_by_region.png')
plt.show()

# --- 3. Histogram: Distribution of Sales Amounts ---
plt.figure(figsize=(8, 6))
plt.hist(df['Sales'], bins=7, color='purple', edgecolor='black')
plt.title('Distribution of Sales Amounts')
plt.xlabel('Sales Amount ($)')
plt.ylabel('Frequency (Number of Sales)')
plt.savefig('3_sales_distribution.png')
plt.show()

# --- 4. Scatter Plot: Relationship between Units Sold and Sales Amount ---
plt.figure(figsize=(8, 6))
plt.scatter(df['Units Sold'], df['Sales'], alpha=0.7, color='green')
plt.title('Sales Amount vs. Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Sales Amount ($)')
plt.grid(True)
plt.savefig('4_sales_vs_units_sold.png')
plt.show()

print("All visualizations have been generated.")

# %%
# =============================================================================
# Any findings or observations
# =============================================================================
print("\n--- Summary of Findings ---")
print("1. **Time Trend:** The line chart shows the fluctuation of sales over the observed period, indicating variability in day-to-day revenue.")
print("2. **Regional Performance:** The bar chart clearly confirms that the 'West' region is the strongest performer in terms of average sales, while the 'South' region lags behind.")
print("3. **Sales Distribution:** The histogram shows that most individual sales transactions fall between $100 and $300, with a few distinct clusters.")
print("4. **Sales Correlation:** The scatter plot reveals a strong, positive, and linear relationship between 'Units Sold' and 'Sales Amount'. This is an expected finding: as more units are sold, the total sales revenue increases proportionally.")