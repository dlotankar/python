import requests, re, json

# get phone no and email from given website

target = 'https://suchicodes.com/contact'

content = requests.get(target).text
phone_numbers = list(set(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", content))) 
emails = list(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", content)))
print(json.dumps({"phone_numbers": phone_numbers,
    "emails" : emails}, indent=4))
