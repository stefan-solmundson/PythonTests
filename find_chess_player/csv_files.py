"""Reading from a CSV File"""

import csv
import itertools

'''
https://docs.python.org/3/library/csv.html#csv.DictReader

File_object = open(r"File_Name","Access_Mode")
r"" prevents a string from allowing special characters like: \t, \n
r  : read only
r+ : read and write
w  : write only
w+ : write and read
a  : append only
a+ : append and read

https://docs.python.org/3/library/csv.html
https://docs.python.org/3/library/csv.html#reader-objects
https://docs.python.org/3/library/csv.html#writer-objects
'''

# 'utf-8' : converts complex characters, making the data easier to work with
with open(r"chess-players.csv", mode='r', newline='', encoding='utf-8') as csvfile:
    # reading the CSV file
    csv_reader = csv.reader(csvfile, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    csv_dict_reader = csv.DictReader(csvfile)

    # displaying the contents of the CSV file
    # for line in csv_reader:
    for line in itertools.islice(csv_reader, 0, 5):
        print(line)

    print()

    for line in itertools.islice(csv_reader, 0, 5):
        print(line[0])

    print()

    for line in itertools.islice(csv_dict_reader, 0, 5):
        print(line)

    print()

    last_name = csv_dict_reader.fieldnames[0]
    for line in itertools.islice(csv_dict_reader, 0, 5):
        print(line[last_name])

    print()

    import operator

    # s = sorted(csvFile1, key=lambda row: row[0])
    csv_sorted = sorted(csv_reader, key=operator.itemgetter(0))
    for line in itertools.islice(csv_sorted, 0, 5):
        print(line)
    for line in itertools.islice(csv_sorted, 0, 5):
        print(line[0])
    print()

    # csvfile.write("This-adds-to-the-end-of-the-file.-")

    # https://docs.python.org/3/library/csv.html#writer-objects
    with open(r"chess-players-sorted.csv", mode='w', encoding='utf-8') as csvfile2:
        # reading the CSV file
        # this replaces the content
        csv_writer = csv.writer(csvfile2, quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        # csv_writer.writerows("test string")
        csv_writer.writerows(csv_sorted)
