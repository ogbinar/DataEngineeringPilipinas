# Import necessary libraries
import pandas as pd

# Define the path to the CSV file on GitHub
github_csv_url = "https://raw.githubusercontent.com/your-username/your-repository/main/your-folder/Import_User_Sample_en.csv"

# Load CSV data into a pandas DataFrame
df = pd.read_csv(github_csv_url)

# Perform transformations as needed
# Example: Convert a column to uppercase
df['Name'] = df['Name'].str.upper()

# Display the transformed data
display(df)

