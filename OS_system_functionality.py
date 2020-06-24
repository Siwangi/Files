"""
cwd: current working directory
chdir : change directory
listdir: list in the directory
mkdir: make one directory
makedirs: make sub directories as well
rmdir: remove one directory
removedirs: remove su directories as well
rename : rename file - use original file then the other file name
"""

import os

##change the directory from where you are which is pycharm to desktop
os.chdir('/Users/siwangishah/Desktop')

##know the path
print(os.getcwd())

##To rename the folder, come out of the folder then use rename and enter old name then new name
# os.rename('Python_file_oper', 'Python_file_Operations')


##to make a directory on the path & make sure you are inside the sample folder or come out on desktop and craete a directoru
# os.mkdir('filename')

#to make subdirectories Samplefolder>Image
# os.makedirs('frstfoldername/second foldername')

##to remove directory -come out of it and use rm
#os.rmdir('samplefolder') ---


## if you wanna delete the complete directory and sub directories
#os.removedirs('frstfoldername/second foldername')


## use open and enter an new filename.txt to write & check with just entering pass

# with open('Shivi_practice.txt', 'w') as f:
#     #write into the text file
#     f.write("Hey!! finally we created a text file in a folder..")
#     f.write('\n')
#     f.write('Yipee!!!!')

##print the list of files in the folder
# print(os.listdir())


##to get the info of the file like size & timestamp and others- ypu need to print with stat command
# print(os.stat('Shivi_practice.txt'))


##to get the size
# print(os.stat('Shivi_practice.txt').st_size)

##to get the last modified timestamp
# print(os.stat('Shivi_practice.txt').st_mtime)


##to check the timestamp/covert the modified time stamp- first import from library of datetime

# from datetime import datetime

# modified_time = os.stat('Shivi_practice.txt').st_mtime
# print(datetime.fromtimestamp(modified_time))

##to check the complete tree (folder & files)

for dirpath, dirnames, dirfilenames in os.walk('/Users/siwangishah/Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', dirfilenames)
    print()



