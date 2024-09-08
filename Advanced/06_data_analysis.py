# 06_data_analysis.py

# This script demonstrates basic data analysis using pandas and matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def analyze_data(df):
    """Perform basic data analysis."""
    print("Data Summary:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

def plot_data(df):
    """Plot data using matplotlib."""
    plt.figure(figsize=(10, 6))
    df['Column1'].hist(bins=30, alpha=0.7, label='Column1')  # Replace 'Column1' with actual column name
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Column1')  # Update title as needed
    plt.legend()
    plt.show()

def main():
    # Load and analyze data
    df = load_data('example_data.csv')  # Replace with your actual data file path
    analyze_data(df)
    plot_data(df)

if __name__ == "__main__":
    main()
