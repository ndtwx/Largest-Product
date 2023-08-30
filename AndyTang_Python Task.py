from math import prod  # Importing the 'prod' function from the 'math' module

def find_largest_multiplied_number(series, length):
    largest_product = 0  # Variable to store the largest product found
    num_digits = len(series)  # Number of digits in the series
    
    # Checking if the 'series' argument is a string enclosed in double quotes
    if not isinstance(series, str) or not series.startswith('"') or not series.endswith('"'):
        raise TypeError("object of type 'int' has no len()")
    
    series = series[1:-1]  # Remove the double quotes from the input string
    
    if length == 0:  # If the 'length' argument is 0, return True
        return True
    if length < 0:  # If the 'length' argument is negative, raise a ValueError
        raise ValueError("Length must not be negative")
    if length > len(series):  # If the 'length' argument is larger than the string length, raise a ValueError
        raise ValueError("Length must be smaller than string length")
    if not series.isdigit():  # If the 'series' argument contains non-digit characters, raise a ValueError
        raise ValueError("Digits input must only contain digits")
    
    # Iterate over all possible subsequences of 'length' digits in the 'series' string
    # Calculate the product of each subsequence and find the maximum product
    return max(prod(map(int, series[i:i+length])) for i in range(num_digits - length + 1))

# Prompt the user to enter the series and length, split the input and assign the values to variables
input_digits, length = input("Enter the series and the length of the series in this format <\"12345\",3>: ").split(",")
# Call the 'find_largest_multiplied_number' function with the input values and print the result
print("Largest multiplied number:", find_largest_multiplied_number(input_digits, int(length)))