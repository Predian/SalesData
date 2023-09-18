import csv
from collections import namedtuple

# Define a named tuple for SalesRecord
SalesRecord = namedtuple('SalesRecord', ['Year', 'Month', 'Amount'])

# Function to parse a CSV file and return a list of SalesRecord objects
def parse_sales_data(file_path):
    sales_data = []
    
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header
        
        for row in reader:
            year = int(row[0])
            month = str(row[1])
            amount = int(row[2])
            sales_data.append(SalesRecord(year, month, amount))
    
    return sales_data

# Main part of the code
if __name__ == '__main__':
    file_path = 'Data/SalesData.csv'
    sales_data = parse_sales_data(file_path)
    
    for record in sales_data:
        print(record)