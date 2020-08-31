'''
- Create a program that asks the user to enter their name and their age.
- Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extra:
- Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
- Print out that many copies of the previous message on separate lines.
'''

import datetime


now = datetime.datetime.now()
# print now.year, now.month, now.day, now.hour, now.minute, now.second

name = input("Please enter your name: ")

# OLD 1
# age_is_valid = False
# age = None
# while not age_is_valid:
#     age = input("Please enter you age: ")
#     if str.isnumeric(age):
#         age = int(age)
#         if age >= 0:
#             age_is_valid = True
# OLD 2
# age_is_valid = False
# age = None
# while not age_is_valid:
#     try:
#         age = int(input("Please enter you age: "))
#         age_is_valid = True
#     except:
#         pass
# NEW
while True:
    age = input("Please enter you age: ")
    if str.isnumeric(age):
        age = int(age)
        if age >= 0:
            break

while True:
    is_birthday_this_year = input("Was your birthday this year? ")
    # is_birthday_this_year = str.lower(input("Was your birthday this year?"))

    if str.lower(is_birthday_this_year[0]).__contains__("y"):
        is_birthday_this_year = True
        break
    elif str.lower(is_birthday_this_year[0]).__contains__("n"):
        is_birthday_this_year = False
        break

year_of_100 = now.year - age + 100 - (is_birthday_this_year * 1)

message = "You will turn 100 in {0}".format(year_of_100)

print(message)

while True:
    repeat = input("How many times would you like to repeat the previous statement? ")
    if str.isnumeric(repeat):
        repeat = int(repeat)
        if repeat >= 0:
            print(((message + "\n") * (repeat - 1)) + message)
            break

print("finished")


