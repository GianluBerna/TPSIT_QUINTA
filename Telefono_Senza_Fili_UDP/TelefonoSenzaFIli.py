import socket as sck

def serverClient():
    host = "192.168.0.127"
    porta = 7000

    server_ip = "192.168.0.130"
    port_ip = 7000

    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    server.bind((host, porta))

    while True:

        data, address = server.recvfrom(4096)

        data = data.decode()

        print(f"da:  {address} messaggio : {data}")

        client.sendto(data.encode(), (server_ip, port_ip))

        print(f"invio a : {server_ip, port_ip} messaggio : {data}")

        if not data or data == "exit":
            print("Close the connection")
            break

        server.sendto(data.encode(), address)

    server.close()
    client.close()

if __name__ == '__main__':
    serverClient()