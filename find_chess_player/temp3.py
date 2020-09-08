import csv

with open(r"chess-players.csv", mode='r', newline='', encoding='utf-8') as csvfile:
    data = csv.reader(csvfile, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for line in data:
        print(line)
