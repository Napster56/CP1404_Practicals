"""
CP18004 Prac09
Program to sort files by extension into different file folders
"""
import os, shutil

__author__ = 'Tyrone Napoli'

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('FilesToSort/')
# print a list of all files (test)
print(os.listdir('.'))
# make new directories
# folders = ('xlsx', 'xls', 'txt', 'png', 'jpg', 'gif', 'docx', 'doc')
# for folder in folders:
#     os.mkdir(folder)

"""
# FromScratch 1
# loop through each file in the (original) directory
for filename in os.listdir('.'):
    # ignore directories, just process files
    if not os.path.isdir(filename):
        # move files by extension to new folders
        if filename.endswith('doc'):
            shutil.move(filename, 'doc/' + filename)
        elif filename.endswith('docx'):
            shutil.move(filename, 'docx/' + filename)
        elif filename.endswith('gif'):
            shutil.move(filename, 'gif/' + filename)
        elif filename.endswith('png'):
            shutil.move(filename, 'png/' + filename)
        elif filename.endswith('jpg'):
            shutil.move(filename, 'jpg/' + filename)
        elif filename.endswith('txt'):
            shutil.move(filename, 'txt/' + filename)
        elif filename.endswith('xls'):
            shutil.move(filename, 'xls/' + filename)
        elif filename.endswith('xlsx'):
            shutil.move(filename, 'xlsx/' + filename)
"""

# From Scratch 2

# use a dictionary for the file extensions
file_extensions = {}
# loop through each file in the (original) directory
for filename in os.listdir('.'):
    # ignore directories, just process files
    if not os.path.isdir(filename):
        new = filename.split('.')[-1]
        file_extensions = file_extensions[new]
        print(file_extensions)
