import re

# Subject String
subject_string = """
John Doe: 123-456-7890 | jane_doe@example.com | Order ID: ORD-45231
Invoice Date: 2023-11-23 | Total: $1,250.00 | Website: https://example.com
File list: report1.pdf, summary.txt, temp_report.txt, image.png
Errors: ERR-1001, ERR-2002 (Critical), ERR-3003 (Ignored)
"""

# 5. Lookaheads and Lookbehinds

# Extract all .txt files not starting with temp using a lookahead
non_temp_txt_files = re.findall(r"(?<!temp_)\b\w+\.txt\b", subject_string)
print(f".txt Files Not Starting with 'temp': {non_temp_txt_files}")

# Find and print currency values preceded by "Total:" using a lookbehind
currency_values = re.findall(r"(?<=Total:\s)\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", subject_string)
print(f"Currency Values Preceded by 'Total:': {currency_values}")

# All error codes (ERR-####) followed by (Critical) using a lookahead
critical_errors = re.findall(r"ERR-\d+(?=\s\(Critical\))", subject_string)
print(f"Critical Error Codes: {critical_errors}")

# 6. Grouping and Validation

# Group and print phone numbers in the format <AreaCode>-<Exchange>-<LineNumber>
phone_numbers = re.findall(r"(\d{3})-(\d{3})-(\d{4})", subject_string)
print(f"Grouped Phone Numbers (AreaCode-Exchange-LineNumber): {phone_numbers}")

# Validate phone numbers that start with the area code 123
valid_phone_numbers = re.findall(r"\b123-\d{3}-\d{4}\b", subject_string)
print(f"Phone Numbers Starting with Area Code 123: {valid_phone_numbers}")

# Validate error codes followed by either (Critical) or (Ignored)
valid_error_codes = re.findall(r"ERR-\d+(?=\s\((?:Critical|Ignored)\))", subject_string)
print(f"Error Codes Followed by (Critical) or (Ignored): {valid_error_codes}")
