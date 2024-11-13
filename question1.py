# question1

# Problem Statement: You have a script that extracts email addresses from a text but needs 
# to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). 
# Modify the script to extract all email addresses except those from the specified domain.

# Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
invalid_emails = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(invalid_emails, text)

print(emails)
