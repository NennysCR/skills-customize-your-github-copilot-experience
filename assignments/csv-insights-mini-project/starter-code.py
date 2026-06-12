# Starter Code: CSV Insights Mini-Project

import csv

# Load the CSV file
with open('data.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print('Total rows:', len(rows))
print('First 5 rows:')
for row in rows[:5]:
    print(row)

# TODO: Add code to compute a summary or comparison
