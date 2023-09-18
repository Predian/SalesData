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

# Function to find the largest amount in the list of SalesRecord objects
def find_largest_amount(sales_data):
    if not sales_data:
        return None  # Return None for an empty list
    
    max_amount_record = max(sales_data, key=lambda record: record.Amount)
    return max_amount_record

# Function to find the smallest amount in the list of SalesRecord objects
def find_smallest_amount(sales_data):
    if not sales_data:
        return None  # Return None for an empty list
    
    min_amount_record = min(sales_data, key=lambda record: record.Amount)
    return min_amount_record

# Function to calculate the average amount in the list of SalesRecord objects
def calculate_average_amount(sales_data):
    if not sales_data:
        return None  # Return None for an empty list
    
    total_amount = sum(record.Amount for record in sales_data)
    average_amount = total_amount / len(sales_data)
    return average_amount

# Main part of the code
if __name__ == '__main__':
    file_path = 'Data/SalesData.csv'
    sales_data = parse_sales_data(file_path)
    
    for record in sales_data:
        print(record)
        
    largest_amount_record = find_largest_amount(sales_data)
    if largest_amount_record:
        print(f"Largest Amount: £{largest_amount_record.Amount} in {largest_amount_record.Year}, {largest_amount_record.Month}")
    else:
        print("No sales data found.")
        
    smallest_amount_record = find_smallest_amount(sales_data)
    if smallest_amount_record:
        print(f"Smallest Amount: £{smallest_amount_record.Amount} in {smallest_amount_record.Year}, {smallest_amount_record.Month}")
    else:
        print("No sales data found.")
        
    average_amount = calculate_average_amount(sales_data)
    if average_amount is not None:
        print(f"Average Amount: £{average_amount:.2f}")
    else:
        print("No sales data found.")