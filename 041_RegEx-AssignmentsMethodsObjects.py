import re

# Subject String
subject_string = """John Doe: 123-456-7890 | jane_doe@example.com | Order ID: ORD-45231
Invoice Date: 2023-11-23 | Total: $1,250.00 | Website: https://example.com
File list: report1.pdf, summary.txt, temp_report.txt, image.png
Errors: ERR-1001, ERR-2002 (Critical), ERR-3003 (Ignored)
"""

# 1. Extracting Key Information ###############################################
# Find and print the first occurrence of a valid email address
email_match = re.search(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}", subject_string)
if email_match:
    print(f"First Email Address: {email_match.group()}")

# Check if the subject string starts with a valid <FirstName> <LastName> format
name_match = re.match(r"[A-Z][a-z]+\s[A-Z][a-z]+", subject_string)
if name_match:
    print(f"Starts with Name: {name_match.group()}")
else:
    print("Does not start with a valid name format.")

# Extract and print all order IDs (e.g., ORD-45231)
order_ids = re.findall(r"ORD-\d+", subject_string)
print(f"Order IDs: {order_ids}")



# 2. Data Redaction ###########################################################
# Replace all error codes (ERR-####) with [ERROR]
redacted_errors = re.sub(r"ERR-\d+", "[ERROR]", subject_string)
print("\nSubject String with Errors Redacted:")
print(redacted_errors)

# Anonymize the email address by hiding the domain (e.g., replace @example.com with @hidden.com)
anonymized_email = re.sub(r"@[\w.-]+", "@hidden.com", subject_string)
print("\nSubject String with Anonymized Email:")
print(anonymized_email)
