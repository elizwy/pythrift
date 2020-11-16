import socket


def server():
    s = socket.socket()
    host = '127.0.0.1'
    port = 6666

    s.bind((host, port))

    s.listen(5)

    while True:
        c, addr = s.accept()
        print('connect addr:', addr)
        c.send("welcome to my space")
        c.close()


if __name__ == '__main__':
    server()
