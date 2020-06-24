import os
import csv

os.chdir('/Users/siwangishah/Desktop/Python_file_Operations')
# print(os.getcwd())
# print(os.listdir())

with open('FG-April4.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader) ##printed just object so need to apply loop to print all the lines before that we need to add a new file to write
    with open('new_fg.csv', 'w') as new_file:
        ##use delimiter for space or hyphens in between the columns(Open the file in textmate to see the difference)(delimiter='\t') is used for tab
        csv_writer = csv.writer(new_file, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)