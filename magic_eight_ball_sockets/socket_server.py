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
import random

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

answers = {
    "positive": [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
    ],
    "neutral": [
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
    ],
    "negative": [
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
}

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        print('Connection details', conn)
        print('Connection address', addr)

        with conn:
            # Prevents the server from closing
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                else:
                    data = data.decode("utf-8")

                    print("data received: \t"
                          + "\t *(utf-8 string of type bytes)\n\t"
                          + data
                          )

                    data = random.choice(
                        answers[random.choice(
                            list(answers.keys())
                        )]
                    )

                    data = data.encode("utf-8")
                    conn.sendall(data)
