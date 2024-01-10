import pandas as pd
import os
from tabulate import tabulate
# Read CSV file into a DataFrame
current_directory = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_directory, "scores.csv")
df = pd.read_csv(file_path, index_col=0)

# Display the DataFrame using tabulate
table = tabulate(df, headers='keys', tablefmt='grid')

# Print the table
print(table)