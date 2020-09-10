'''
Task:
1) Search "the Net" for ways to monitor temperature on Windows, Linux, Mac, Raspian,
'''

# pip3 install psutil --user
import psutil

if __name__ == '__main__':
    temperatures = psutil.sensors_temperatures()
    print(temperatures)


# def length_recursive(s):
#     count = 0
#
#     def is_char(c):
#         c = c.lower()
#         ans=''
#         for s in c:
#             if s in 'abcdefghijklmnopqrstuvwxyz':
#                 ans += s
#         return ans
#
#     def length(s):
#         global count
#         if len(s)==0:
#             return count
#         else:
#             count += 1
#             return length(s[1:])
#
#     return length(is_char(s))
#
#
# print(length_recursive())