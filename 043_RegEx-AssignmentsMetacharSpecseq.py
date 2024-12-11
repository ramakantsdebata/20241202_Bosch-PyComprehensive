import re

# Subject String
subject_string = """
John Doe: 123-456-7890 | jane_doe@example.com | Order ID: ORD-45231
Invoice Date: 2023-11-23 | Total: $1,250.00 | Website: https://example.com
File list: report1.pdf, summary.txt, temp_report.txt, image.png
Errors: ERR-1001, ERR-2002 (Critical), ERR-3003 (Ignored)
"""

## 3. Patterns and Matching
# Extract all numeric values, including phone numbers, dates, and order IDs
numeric_values = re.findall(r"\d{4}-\d{2}-\d{2}|\d{3}-\d{3}-\d{4}|\bORD-\d+\b", subject_string)
print(f"Numeric Values (Dates, Phone Numbers, Order IDs): {numeric_values}")

# Match and print dates in the format YYYY-MM-DD
dates = re.findall(r"\d{4}-\d{2}-\d{2}", subject_string)
print(f"Dates (YYYY-MM-DD): {dates}")

# Match and print file names with .txt extensions
txt_files = re.findall(r"\b\w+\.txt\b", subject_string)
print(f"File Names with .txt Extensions: {txt_files}")

## 4. Analyzing Words
# Count the number of alphanumeric words containing underscores (_)
underscore_words = re.findall(r"\b\w*_\w*\b", subject_string)
print(f"Words with Underscores: {underscore_words} (Count: {len(underscore_words)})")

# Find and print words starting with the letter r
words_starting_with_r = re.findall(r"\br\w*", subject_string, re.IGNORECASE)
print(f"Words Starting with 'r': {words_starting_with_r}")

# Find and print words ending with .pdf or .png
files_with_specific_extensions = re.findall(r"\b\w+\.(?:pdf|png)\b", subject_string)
print(f"Words Ending with .pdf or .png: {files_with_specific_extensions}")
