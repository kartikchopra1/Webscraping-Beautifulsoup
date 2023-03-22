import pandas as pd

data = pd.read_html('https://sportsgamestoday.com/f1-tv-schedule.php')

for i, table in enumerate(data):
    # Write the DataFrame to a CSV file
    table.to_csv(f'f1_tv_schedule_{i}.csv', index=False)
    print(f"CSV file f1_tv_schedule_{i}.csv written successfully.")
# To write both tables extracted from the webpage to separate CSV files,
# you can loop through the list of DataFrames returned by pd.read_html()
# and write each DataFrame to a separate file. Here's an example code:
# In this code, we use a for loop to iterate through the
# list of DataFrames returned by pd.read_html().
# For each DataFrame, we use the to_csv() method to write its contents to a separate CSV file
# named "f1_tv_schedule_0.csv" for the first DataFrame, and "f1_tv_schedule_1.csv"
# for the second DataFrame. We also include an index in the filename to differentiate
# between the two files. The index = False parameter is used to exclude the DataFrame
# index from the CSV output.
# The print() statement is used to confirm that each file was written successfully.

# --------------------------f1 table ----------------------------------

data = pd.read_html('https://sportsgamestoday.com/f1-tv-schedule.php')
table = data[0]

# Write the DataFrame to a CSV file
table.to_csv('f1_tv_schedule.csv', index=False)

print("CSV file written successfully.")

# To write the contents of the table DataFrame to a CSV file, you can use the to_csv()
# method from pandas. Here's an example code that writes the contents of the table
# DataFrame to a file named "f1_tv_schedule.csv":

# This code reads the F1 TV schedule table from the specified URL and assigns it to the table variable,
# as before. The to_csv() method is then used to write the contents of the table DataFrame to a
# file named "f1_tv_schedule.csv". The index = False parameter is used to exclude the DataFrame
# index from the CSV output.

# The last line of the code prints a message to confirm
# that the CSV file was written successfully.
