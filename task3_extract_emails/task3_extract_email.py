import re


input_file = open('input.txt', 'r')
text = input_file.read()
input_file.close()


email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
found_emails = re.findall(email_pattern, text)


output_file = open('emails.txt', 'w')
for email in found_emails:
    output_file.write(email + '\n')
output_file.close()

print("\nEMAILS HAVE BEEN EXTRACTED!!!")