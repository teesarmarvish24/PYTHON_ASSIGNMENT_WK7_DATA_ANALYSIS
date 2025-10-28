# PYTHON_ASSIGNMENT_WK7_DATA_ANALYSIS

This is the solution for the data analysis assignment from plp which i enjoyed the most. Big thanks to plp academy for such a wonderful assignment

# Python Data Analysis with Pandas and Matplotlib

## Project Overview

This project is an assignment focused on the fundamentals of data analysis using Python. It demonstrates how to load, clean, analyze, and visualize a dataset using the **pandas**, **matplotlib**, and **seaborn** libraries. The project uses a sample sales dataset to perform basic analysis and generate several common plot types.

---

## objectives

- To load and explore a dataset using the pandas library.
- To clean data by handling missing values and correcting data types.
- To perform basic data analysis, such as calculating descriptive statistics and grouping data.
- To create simple plots and charts with the matplotlib library for data visualization.

---

## Dataset

The script uses a self-generated sample dataset named `sales_data.csv`. This dataset is created by the script itself during the first run and contains the following columns:

- **Date**: The date of the sale (datetime).
- **Region**: The sales region (categorical).
- **Product**: The product identifier (categorical).
- **Sales**: The total sales amount (numerical).
- **Units Sold**: The number of units sold (numerical).

---

## 🛠️ Libraries Used

- **pandas**: For data loading, manipulation, and analysis.
- **numpy**: Used to create sample data and handle numerical operations.
- **matplotlib**: For creating static, animated, and interactive visualizations.
- **seaborn**: For enhancing the visual style of the plots.

---

## 🚀 How to Run the Code

1.  **Ensure libraries are installed:**

    ```bash
    pip install pandas matplotlib seaborn
    ```

2.  **Run the Python Script:**
    Save the code as `analysis.py` (or any name you prefer) in a project folder.

    ```bash
    python analysis.py
    ```

3.  **Output:**
    - The script will first create the `sales_data.csv` file in the same directory.
    - It will print the analysis results (like `df.head()`, `df.describe()`, and group means) directly to your terminal.
    - It will generate and save the following four image files in your project folder:
      - `1_sales_over_time.png`
      - `2_average_sales_by_region.png`
      - `3_sales_distribution.png`
      - `4_sales_vs_units.png`

---

## Analysis and Visualizations

This project successfully completes all assigned tasks:

### Task 1: Data Loading and Cleaning

- Loaded the `sales_data.csv` file.
- Inspected the first 5 rows using `.head()`.
- Checked for missing values and incorrect data types using `.info()`.
- Filled one missing `Sales` value with the column mean.
- Converted the `Date` column from an object to a `datetime` type.

### Task 2: Basic Data Analysis

- Calculated descriptive statistics (mean, median, std, etc.) for numerical columns using `.describe()`.
- Grouped data by `Region` to find the mean `Sales`.
- Grouped data by `Product` to find the total `Units Sold`.

### Task 3: Data Visualization

Four plots were generated and saved:

1.  **Line Chart**: Shows the trend of total sales over time.
2.  **Bar Chart**: Compares the average sales across different regions.
3.  **Histogram**: Shows the frequency distribution of sales amounts.
4.  **Scatter Plot**: Visualizes the relationship between 'Units Sold' and 'Sales Amount'.

---

## Summary of Findings

1.  **Regional Performance**: The **West** region has the highest average sales, indicating it is the strongest market.
2.  **Sales Distribution**: Most sales transactions fall between $100 and $300.
3.  **Sales Correlation**: There is a strong, positive linear relationship between _Units Sold_ and _Sales Amount_. This confirms that as more units are sold, the total revenue increases proportionally.
