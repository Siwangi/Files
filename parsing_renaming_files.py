
##to work on OS, import
import os

##change directory from Pycharm to Desktop
os.chdir('/Users/siwangishah/Desktop/Python_file_Operations/Shivi_python folder')
print(os.getcwd())

##to list down files in the directory
for file in os.listdir():
    ##to split the extension from the filename
    print(os.path.splitext(file))

    ##Set variable for the Tuple
    # file_name, file_ext = os.path.splitext(file)

    ##print to check the filename without extensions
    # print(file_name)

    ## print to spilt hyphen
    # print(file_name.split('_'))

    ##name the variables to set each of the words in filename
    # file_Kind, file_num = file_name.split('_')
    # print(file_num)

    ##set format to rename the file as per requirement
    # file_Kind, file_num = file_name.split('_')

    ## to remove white space use strip
    # file_Kind=file_Kind.strip()
    # file_num=file_num.strip()

    ##can use [1:] to remove anything from first postion in strip command
    ## can use .zfill(2) -- it will enter 01 if there is 1 in the file name in strip command

    # new_name = '{}-{}-'.format(file_Kind,  file_ext)

    # os.rename(file, new_name)




