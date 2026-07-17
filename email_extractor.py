import re

# Input and output file names
input_file = "input.txt"
output_file = "extracted_emails.txt"

try:
    # Read the input file
    with open(input_file, "r") as file:
        text = file.read()

    # Regular expression to find email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    # Remove duplicate email addresses
    unique_emails = list(set(emails))

    # Save extracted emails
    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    # Display results
    print("=" * 40)
    print("EMAIL EXTRACTION COMPLETED")
    print("=" * 40)
    print(f"Total Emails Found: {len(unique_emails)}\n")

    for email in unique_emails:
        print(email)

    print(f"\nEmails have been saved to '{output_file}'.")

except FileNotFoundError:
    print("Error: input.txt file not found.")