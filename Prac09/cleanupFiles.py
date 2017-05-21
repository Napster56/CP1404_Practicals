"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil, re

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('Lyrics/Christmas/temp')
# print a list of all files (test)
# print(os.listdir('.'))

# make a new directory
# os.mkdir('temp')

# loop through each file in the (original) directory
# for filename in os.listdir('.'):
#    # ignore directories, just process files
#    if not os.path.isdir(filename):
#        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
#        print(new_name)
#        # Option 1: rename file to new name - in place
#        os.rename(filename, new_name)
#        # Option 2: move file to new place, with new name
#        shutil.move(filename, 'temp/' + new_name)


for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        new = filename.split("_")
        for name in new:
            name.capitalize()
        print(new)

            #print(new2)
    #new = "".join(filename)
    #
        #new = "".join(new)

        #print(new)
        #filename.replace(name, new)
        #print(filename)
    #if len(filename) == 1:
    #    new_file = re.findall('[A-Z][^A-Z]*', filename)
    #    new = " ".join(new_file)
    #    filename.replace(filename, new)
    #print(filename)
    #
    #for name in new_name:
    #    name.capitalize()
    #    new = " ".join(new_name)
    #    print(new)
    #    filename.replace(name, new)
    #

    # print(new)
    # if len(new_name) == 1:
    #    new_file = re.findall('[A-Z][^A-Z]*', new)
    ##    filename.replace(new_name, new_file)                        )
    # else:
    #    filename.replace(new, str(new_file))
    # for name in new_name:
    #    name.capitalize()
#
#    filename.replace(name, new)
# print(filename)
# print(type(new))





# new_name.append(name)
# print(new_name)
# for word in filename:

#    word.capitalize()
#    print(filename)

# for name, filename in titles:
#    print(filename.title())
'''
# Processing subdirectories using os.walk()
os.chdir('..')
for dir_name, subdir_list, file_list in os.walk('.'):
    print("In", dir_name)
    print("\tcontains subdirectories:", subdir_list)
    print("\tand files:", file_list)
'''
