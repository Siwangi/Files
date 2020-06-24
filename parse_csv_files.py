import os

import csv

os.chdir('/Users/siwangishah/Desktop/Python_file_Operations')
# print(os.getcwd())
# print(os.listdir())

with open('FG-Tos-users-june.csv', 'r') as csv_file:
    ##set variable
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)
    # next(csv_reader)
    for line in csv_reader:
        ## when you use reader and writer library, u need to pass the index to read
        #add loop to print each line & for only showing a particular column, we count header as index. so for this file index starts from 0 to 19)
        print(line[1], line[2])
        ## if wanna exclude the first line which is header use command next(variable in which the reader is set) before the loop