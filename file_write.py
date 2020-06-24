## to open and write in the same read file(read mode), error appears- file is not writable as wr have given 'r' in the command .
## to write we need to add 'w' & to append we need to add 'a' & have opened the file in the write mode

"""
To write file-  if there is no such file in the directory, it will create a new file. Also insert 'w' instead of 'r'
& if there is already a file with the same name, it will over ride it
& if you dont wanna override in the same file use 'a' instead of 'w' to append in the file
"""

## craete a new txt file and write to it
with open('sample_file1.txt', 'w') as f:

    ## use pass just to create a new file and do nothing(see in the directory- new file has been craeted)
    # pass

    ## to actually write in the new created file, use write command & remove pass statement (file will have the text that you entered in the write statement also use \n to print in next line
    f.write('Shivangi')
    f.write("\n")
    f.write("Shivangi has started coding 2 months back")

    ## to override the first statement and start the second statement for begininng use seek(0)
    # f.write('Shivangi')
    # f.seek(0)
    # f.write("Shivangi has started coding 2 months back")

    ##seek can be used to replace the character (test- place r at postion 0- it will print Rest)
    # f.write('Test')
    # f.seek(0)
    # f.write('R')
