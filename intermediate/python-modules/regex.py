phone = "(555)-555-5555"

r'(\d\d\d)-\d\d\d-\d\d\d\d'

r'(\d{3})-\d{3}-\d{4}'

## ----------------------------
## ----------------------------

text = "The agent's phone number is 408-555-1234. Call soon"

print('phone' in text)

import re

pattern = 'phone'

match = re.search(pattern, text)

print(match)

print(match.span())

print(match.end())

print(match.start())

matchAll = re.findall(pattern, text)

for singleMatch in re.finditer('phone', text):
    print(singleMatch)

print("-------------------------")

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)

print("----------------------------------")

phone_patterns = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_patterns, text)

print(results.group())
print(results.group(1))