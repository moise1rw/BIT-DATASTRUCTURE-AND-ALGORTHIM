
#1.Integers


# Example waste collection values (in kilograms)
waste_quantities = [120, 150, 90, 200, 175]
total_waste = sum(waste_quantities)

average_waste = total_waste / len(waste_quantities)

min_waste = min(waste_quantities)
max_waste = max(waste_quantities)
print("Integer Operations:")
print("Total waste collected:", total_waste, "kg")
print("Average waste collected:", average_waste, "kg")
print("Minimum waste collected:", min_waste, "kg")
print("Maximum waste collected:", max_waste, "kg")




#2.string
# Waste Collection Tally - String Operations
#For example waste collection values (in kilograms)
waste_quantities = [120, 150, 90, 200, 175]

total_waste = sum(waste_quantities)
average_waste = total_waste / len(waste_quantities)
#TO Create a formatted string report using f-strings
report = (
    f"--- Waste Collection Report ---\n"
    f"Total Waste Collected: {total_waste} kg\n"
    f"Average Waste Collected: {average_waste:.2f} kg\n"
)

#TO  Display the report
print("Formatted String Report:")	
print(report)
#3.BOOLEAN
#TO CREATE Waste Collection Tally - Boolean Operations

#FOR Example waste collection values (in kilograms)
waste_quantities = [120, 150, 90, 200, 175]


total_waste = sum(waste_quantities)
average_waste = total_waste / len(waste_quantities)
max_waste = max(waste_quantities)


threshold = 140

#Boolean condition with compound check
if average_waste > threshold and max_waste > 180:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
 

#4. LIST

# Waste Collection Tally - List Operations

# Example waste collection values (in kilograms)
waste_quantities = [120, 150, 90, 200, 175]

print("Before modification:", waste_quantities)

# Add a new record (e.g., another day's waste collection)
waste_quantities.append(160)

# Remove values less than 100 (filter out small/unusual entries)
waste_quantities = [x for x in waste_quantities if x >= 100]

# Sort the list
waste_quantities.sort()

print("After modification:", waste_quantities)
#5.ARRAY
# Waste Collection Tally - Array Operations

import array

# Create a Python array with integer type ('i' = signed int)
waste_array = array.array('i', [120, 150, 175, 200])

# Calculate the sum of the array
array_sum = sum(waste_array)

# For comparison, let's also use a list version
waste_list = [120, 150, 175, 200, 160]  # (example updated list)
list_sum = sum(waste_list)

# Display results
print("Array values:", waste_array.tolist())
print("Sum of array:", array_sum)
print("Sum of list:", list_sum)

# Compare sums
if array_sum == list_sum:
    print("Comparison: Equal")
else:
    print("Comparison: Not Equal")


#6.DICTIONARY

# Waste Collection Tally - Dictionary Operations

# List of dictionaries for different zones
waste_records = [
    {"id": 1, "name": "Zone A", "value": 120},
    {"id": 2, "name": "Zone B", "value": 150},
    {"id": 3, "name": "Zone C", "value": 90},
]

print("Before update/delete:", waste_records)

# Update: Change Zone B's value
waste_records[1]["value"] = 160

# Delete: Remove Zone C
waste_records = [rec for rec in waste_records if rec["id"] != 3]

# Compute total value from all records
total_value = sum(rec["value"] for rec in waste_records)

print("After update/delete:", waste_records)
print("Total value from dictionaries:", total_value, "kg")



