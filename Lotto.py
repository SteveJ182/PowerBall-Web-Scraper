import csv
from datetime import datetime

# Initialize dictionaries to store counts for each number in each column
number_counts = {f'Number {i}': {str(num): 0 for num in range(1, 70)} for i in range(1, 6)}
powerball_counts = {str(num): 0 for num in range(1, 27)}  # Initialize dictionary for Powerball numbers (1-26)
power_play_counts = {str(num): 0 for num in [2, 3, 4, 5, 10]}  # Initialize dictionary for Power Play numbers (2, 3, 4, 5, 10)

# Date threshold
start_date = datetime.strptime("10/03/2015", "%m/%d/%Y")

# Open the CSV file for reading
with open('powerball_draws.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row if it exists
    next(csv_reader)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract the date from the row
        date_str = row[0]  # Assuming the date is in the first column
        date = datetime.strptime(date_str, "%m/%d/%Y")
        
        # Check if the date is on or after the start date
        if date >= start_date:
            # Extract regular numbers from each column
            for i, number in enumerate(row[1:6], start=1):
                number_counts[f'Number {i}'][number] += 1
            
            # Extract Powerball number if the row contains enough elements
            if len(row) > 6:
                powerball_number = row[6]
                if powerball_number and powerball_number.isdigit() and 1 <= int(powerball_number) <= 26:
                    powerball_counts[powerball_number] += 1
                else:
                    print(f"Warning: Invalid Powerball number '{powerball_number}' encountered.")
            
            # Extract Power Play number if the row contains enough elements
            if len(row) > 7:
                power_play_number = row[7]
                if power_play_number and power_play_number.isdigit() and int(power_play_number) in [2, 3, 4, 5, 10]:
                    power_play_counts[power_play_number] += 1
                else:
                    print(f"Warning: Invalid Power Play number '{power_play_number}' encountered.")
        else:
            # Stop reading the file once a row with an earlier date is encountered
            break

# Save the initial results to a file
output_file_initial = 'number_counts_initial.txt'

with open(output_file_initial, 'w') as file:
    file.write("Regular Numbers:\n")
    for column, counts in number_counts.items():
        file.write(f"{column}:\n")
        for number, count in counts.items():
            file.write(f"    Number {number}: {count}\n")

    file.write("\nPowerball Numbers:\n")
    for number, count in powerball_counts.items():
        file.write(f"    Number {number}: {count}\n")

    file.write("\nPower Play Numbers:\n")
    for number, count in power_play_counts.items():
        file.write(f"    Number {number}: {count}\n")

print(f"Initial results saved to {output_file_initial}")

# Sort the counts from most to least frequent
sorted_number_counts = {column: dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)) for column, counts in number_counts.items()}
sorted_powerball_counts = dict(sorted(powerball_counts.items(), key=lambda x: x[1], reverse=True))
sorted_power_play_counts = dict(sorted(power_play_counts.items(), key=lambda x: x[1], reverse=True))

# Save the sorted results to a file
output_file_sorted = 'number_counts_sorted.txt'

with open(output_file_sorted, 'w') as file:
    file.write("Regular Numbers:\n")
    for column, counts in sorted_number_counts.items():
        file.write(f"{column}:\n")
        for number, count in counts.items():
            file.write(f"    Number {number}: {count}\n")

    file.write("\nPowerball Numbers:\n")
    for number, count in sorted_powerball_counts.items():
        file.write(f"    Number {number}: {count}\n")

    file.write("\nPower Play Numbers:\n")
    for number, count in sorted_power_play_counts.items():
        file.write(f"    Number {number}: {count}\n")

print(f"Sorted results saved to {output_file_sorted}")

from collections import deque
from collections import Counter

# Initialize dictionaries to store counts for each number in each column
number_counts = {f'Number {i}': Counter() for i in range(1, 6)}
powerball_counts = Counter()  # Initialize Counter for Powerball numbers (1-26)
power_play_counts = Counter()  # Initialize Counter for Power Play numbers (2, 3, 4, 5, 10)

# Keep track of the first 20 lines
first_20_lines = deque(maxlen=20)

# Open the CSV file for reading
with open('powerball_draws.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row if it exists
    next(csv_reader)
    
    # Read the first 20 lines and store them
    for _ in range(20):
        row = next(csv_reader)
        first_20_lines.append(row)

# Process the first 20 lines
for row in first_20_lines:
    # Extract regular numbers from each column
    for i, number in enumerate(row[1:6], start=1):
        number_counts[f'Number {i}'][number] += 1
    
    # Extract Powerball number if the row contains enough elements
    if len(row) > 6:
        powerball_number = row[6]
        if powerball_number and powerball_number.isdigit() and 1 <= int(powerball_number) <= 26:
            powerball_counts[powerball_number] += 1
    
    # Extract Power Play number if the row contains enough elements
    if len(row) > 7:
        power_play_number = row[7]
        if power_play_number and power_play_number.isdigit() and int(power_play_number) in [2, 3, 4, 5, 10]:
            power_play_counts[power_play_number] += 1

# Get the 3 most frequent numbers for each column
most_frequent_numbers = {f'Number {i}': counts.most_common(3) for i, counts in number_counts.items()}
most_frequent_powerballs = powerball_counts.most_common(3)
most_frequent_powerplays = power_play_counts.most_common(3)

# Print the results
print("3 Most Frequent Numbers for Each Column:")
for column, numbers in most_frequent_numbers.items():
    print(f"{column}: {numbers}")
print("Most Frequent Powerball Numbers:", most_frequent_powerballs)
print("Most Frequent Power Play Numbers:", most_frequent_powerplays)