import os
import csv

os.chdir('/Users/siwangishah/Desktop/Python_file_Operations')

with open('FG-April4.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('fg_new2.csv', 'w') as new_file:
        ##for Dictwriter we need to add field names
        fieldnames = ['first-name (S)', 'last-name (S)', 'email (S)', 'org-user-id (S)']
        #'role-id (S)', 'store-id (S)'
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        ##to get the header in the new file we need to write a command
        csv_writer.writeheader()

        for line in csv_reader:
            del line['role-id (S)']
            del line['store-id (S)']
            csv_writer.writerow(line)

            """ using reader and writer library we need to modify the column by printing the index
            but in dictionary we need to exclude the specific fieldname from the fieldnames variable and 
            enter the del command with the fieldname"""