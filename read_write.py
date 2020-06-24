"""
use 'r' as read the file &
'rf' denotes readfile(filename) since this is the file that we are going to read from inorder to write in our copy file
Need to create another copy to write into so use 'wf' (writefile-filename) with 'w' in the other statement
(how to work with multiple files by putting the same code(read & write) in two lines)

"""

with open('sample_file.py', 'r') as rf:
    with open('sample_file_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


"""
to open the picture file(.jpg) - we need to open the file in binary mode and to do that use 'rb' instead of 'r' & 'wb' instead of 'w'
"""

