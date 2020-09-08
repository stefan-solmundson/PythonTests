# Reading from a CSV File

import csv
import codecs
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
'''

# types_of_encoding = ["utf8", "cp1252"]
types_of_encoding = ["utf8"]
for encoding_type in types_of_encoding:
    # Opening the CSV file
    # csvfile = codecs.open(r"chess-players.csv", encoding=encoding_type, errors='replace')
    # csvfile.close()
    # OR
    with codecs.open(r'chess-players.csv', mode="r+", encoding=encoding_type, errors='replace') as csvfile:
        # reading the CSV file
        csv_reader = csv.reader(csvfile)
        csv_dict_reader = csv.DictReader(csvfile)
        # csv.DictReader()

        # displaying the contents of the CSV file
        for line in csv_reader:
        # for line in itertools.islice(csv_reader, 0, 5):
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

        # with codecs.getwriter(encoding_type) as csvwriter:
        #
        #     csvwriter.
        # with csv.writer(r"chess-player-sorted.csv") as csvwriter:
        # csvwriter =
        csvfile.write("this adds to the end of the file")
        # TODO: Write to a different file called chess-players-sorted.csv
        with codecs.open(r'chess-players-sorted.csv', mode="w", encoding=encoding_type, errors='replace') as csvfile2:
            csvfile2.write(csv_sorted)
            csvfile2.writer(f)
        # x = csv.writer(csvfile)
        # x = codecs.getwriter(encoding_type)
        # csvfile.encoding()
        # x.
        # x.wr



        # if reaches end, there's no point using a different decoder
        break
