f = open('fileone.txt', 'w+')
f.write('FIRST FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('FILE 2')
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

## ------------------------


zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
print(zip_obj.extractall('extrated'))
zip_obj.close()



import shutil

shutil.make_archive('outro_zip', 'zip', 'extrated')