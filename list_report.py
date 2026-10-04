# list_report.py
# Week 7 - Part C: List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 2. Print each item numbered
print("Numbered list:")
number = 1
for item in items:
    print(f"{number}. {item}")
    number += 1

# 3. Count item names with more than 4 letters
count = 0
for item in items:
    if len(item) > 4:
        count += 1
print("\nItems with more than 4 letters:", count)

# 4. Find the longest item name (manual comparison, no max())
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
print("Longest item name:", longest)
