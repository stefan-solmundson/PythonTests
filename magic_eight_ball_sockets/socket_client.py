"""
# Magic 8-Ball

Write a program that uses pipes or sockets for inter-process communication. The program should
implement a so-called Magic 8-ball, which you can ask questions. The Magic 8-ball then answers with
a specific reply. The replies can be found here: https://en.wikipedia.org/wiki/Magic_8-Ball.

You can decide how you want to determine the reply (for instance, you can use the question to calculate a
hash that determines the answer, perhaps adding a bit of randomness so it doesn’t always reply with
exactly the same answer for a certain question).

You’ll be implementing a simple client-server architecture, where the server implements the Magic 8-ball.

--

Tutorial : https://realpython.com/python-sockets/
GitHub files : https://github.com/realpython/materials/tree/master/python-sockets-tutorial
"""

# !/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    question = input("Please enter a question.\n")
    question = question.encode("utf-8")
    s.sendall(question)
    data = s.recv(1024)

print('Received', repr(data))
