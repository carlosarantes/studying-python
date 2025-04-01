import os

os.getcwd()

print(os.listdir())

import shutil

shutil.move('file.txt', '/destination')

os.unlink('....')

os.rmdir('...')

shutil.rmtree('...')

import send2trash

send2trash.send2trash('....')


for folder, sub_folder, files in os.walk():
    for ff in files:
        print(ff)