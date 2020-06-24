import os
import csv

os.chdir('/Users/siwangishah/Desktop/Python_file_Operations')

## To match the headers with line value in each rows: use DictReader to separate every line with headers
with open('FG-April4.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        ##to print the complete line
        print(line)
        ##to find any specific column
        print(line['email (S)'])
        
