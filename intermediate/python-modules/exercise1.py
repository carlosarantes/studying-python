import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip', '', 'zip')

import re

with open('extracted_content/Instructions.txt') as file:
    content = file.read()
    print(content)

    pattern = r'\d{3}-\d{3}-\d{4}'

    test_string = 'here is a phone number 555-123-1234'

    re.findall(pattern, test_string)

    file.close()

def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    ff = open(file, 'r')
    text = ff.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''
    
import os 

results = []

for folder, sub_folders, files in os.walk(os.getcwd()):
    for fff in files:
        full_path = folder+''
        print(full_path)
        results.append(search(full_path))
