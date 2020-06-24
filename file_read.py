## Best practice
## Open a file to read
## f denotes file

with open('sample_file.py', 'r') as f:

    ## to read the file (main command which is placed in a variable
    # f_contests = f.read()

    ## to read the lines in the file
    # f_contests = f.readlines()

    ## to read the first line of the file
    # f_contests=f.readline()

    ## again read the next line of the file(it will print the next line if the above code is still present which is same
    # f_contests=f.readline()

    ##print statements ends with a new line by default so we can add empty string at the end so that print statement doesnt add a new line
    ## to print in the same way as in file and not ignore the first line print empty string at the end (use end='')
    # f_contest = f.readline()
    # print(f_contest, end= '')

    # f_contest = f.readline()
    # print(f_contest, end= '')

    ## to read all the lines one by one instead of printing everytime, we can apply loop to iterate
    # for line in f:
    #     print(line, end='')

    ## if wanna read exact lines like 100 characters of the line or some content of the file (it calculates space as well as character)
    # f_contests=f.read(20)
    # print(f_contests, end='*')

    ## to print lines after 50th - again print the same code(repeat if needed to print more lines) & if the lines are completed, read will return an empty string or use * to see where the 10th character ends
    # f_contests=f.read(50)
    # print(f_contests, end='*')

    ## to see the current position
    # print(f.tell())

    ## when not to hard code and set a variable with limit initially:
    # size_to_read = 50
    # f_contests = f.read(size_to_read)
    # print(f_contests, end='')

    ## to start from any position(which can be begining or 0) instead of to start from where we left off(like we saw above if we print 2 times or again the same command it prints one line then other) to avoid that use seek command
    size_to_read=50

    f_contests = f.read(size_to_read)
    print(f_contests)

    f.seek(10)

    f_contests = f.read(size_to_read)
    print(f_contests)

















"""

    # print(f_contests)
    # print(f.name)
# print(f.read())

## To start of : this way can be used as well instaed of usng as (start of code which is optional)

# f = open('sample_file.py', 'r')

## to close the file
# f.close()

"""





