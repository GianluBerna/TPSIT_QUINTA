import re
import socket as sck
import Classi.Config as conf
from Classi.AlphaBot import AlphaBot as AlphaBot


# 0.0,B50R90F600L90F400
# B 50  R 90    F 600   L 90    F 400
# [(b, 50), ]s


def client():
    print("creo istanza")
    c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # instantiate

    c.connect((conf.SERVER_IP, conf.SERVER_PORT))
    print("connect")

    print("Enter 'exit' to end the connection")
    msg = input("->")  # take input
    alphabot = AlphaBot()
    while True:
        try:
            c.sendall(msg.encode())  # send message
        except:
            print(f"failed")

        data = c.recv(conf.BUFFER_SIZE).decode()  # receive response
        print(f"Received from server: {data}")  # show response

        data = (data.split(","))[1]
        lista_potenze = re.split('B|R|F|L', data)
        lista_potenze.pop(0)
        regex = ''
        for index, el in enumerate(lista_potenze):
            if index == len(lista_potenze) - 1:
                regex += el
            else:
                regex += el + '|'
        lista_direzioni = re.split(regex, data)
        lista_direzioni.pop(-1)
        comandi = []
        for index, el in enumerate(lista_potenze): comandi.append((lista_direzioni[index], int(el)))
        print(comandi)
        for el in comandi: istruction(alphabot, el[0], el[1])

        msg = input("->")  # again take input

        if msg == "exit":
            c.sendall(msg.encode())  # send message
            print("Close the connection")
            break

    c.close()  # close the connection


def istruction(alphabot, command, number):
    switcher = {
        "F": alphabot.forward,
        "B": alphabot.backward,
        "R": alphabot.right,
        "L": alphabot.left
    }
    switcher[command](number)

if __name__ == '__main__':
    client()
