#!/usr/bin/env python3
import csv

input_file = "dict_searches.csv"
output_file = "output.csv"

# Create a dictionary to store the latest datetime for each string
string_dict = {}

# Read the input CSV file
with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in reader:
        datetime_str = row[0]
        string = row[1]

        # Check if the string is already in the dictionary
        if string in string_dict:
            # Compare the datetime with the one in the dictionary
            if datetime_str > string_dict[string]:
                string_dict[string] = datetime_str
        else:
            string_dict[string] = datetime_str

# Write the filtered data to the output CSV file
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

    # Iterate over the dictionary and write the rows to the output file
    for string, datetime_str in string_dict.items():
        writer.writerow([datetime_str, string])

print("Duplicate lines removed and saved to output.csv.")
