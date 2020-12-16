import socket as sck


def serverClient():
    host = "192.168.88.83"
    porta = 7000

    server_ip = "192.168.88.85"
    port_ip = 7000

    server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    server.bind((host, porta))

    while True:
        server.listen()
        conn, address = server.accept()

        print(f"Connesso con : {conn}")
        data = conn.recv(4096)

        data = data.decode()

        print(f"da:  {address} messaggio : {data}")

        client.connect((server_ip, port_ip))
        client.sendall(data.encode())

        print(f"invio a : {server_ip, port_ip} messaggio : {data}")

        if not data or data == "exit":
            print("Close the connection")
            break

        conn.sendall(data.encode(), address)

    conn.close()
    client.close()


if __name__ == '__main__':
    serverClient()
