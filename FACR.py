import socket
import threading
import os
import time
import sys
os.system("clear")
print( """
	        
                             ╭━━━┳━━━┳━━━┳━━━╮
                             ┃╭━━┫╭━╮┃╭━╮┃╭━╮┃
                             ┃╰━━┫┃╱┃┃┃╱╰┫╰━╯┃
                             ┃╭━━┫╰━╯┃┃╱╭┫╭╮╭╯
                             ┃┃╱╱┃╭━╮┃╰━╯┃┃┃╰╮
                             ╰╯╱╱╰╯╱╰┻━━━┻╯╰━╯
                             server v 1.2 | StRaNgEdReAmEr
	                     for queries: oohacker008@gmail.com
""")
def loading_animation():
    for i in range(100):
        sys.stdout.write("\rLoading... %d%%" % (i+1) * 10)
        sys.stdout.flush()
        time.sleep(0.1)

if __name__ == "__main__":
    loading_animation()
    print("\nLoading complete!")

def start_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(10)
    print("Server started at", ip, ":", port)
    clients = []
    while True:
        client_socket, address = server_socket.accept()
        print("Accepted connection from", address)
        client_socket.send("Welcome to the chat server!".encode())
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_thread.start()

def handle_client(client_socket, clients):
    username = client_socket.recv(1024).decode()
    broadcast(clients, username + " has joined the chat!", client_socket)
    while True:
        message = client_socket.recv(1024).decode()
        if message == "exit":
            broadcast(clients, username + " has left the chat!", client_socket)
            client_socket.send("Goodbye!".encode())
            client_socket.close()
            clients.remove(client_socket)
            break
        else:
            broadcast(clients, username + ": " + message, client_socket)

def broadcast(clients, message, sender):
    for client_socket in clients:
        if client_socket != sender:
            client_socket.send(message.encode())

if __name__ == '__main__':
    ip = input("Enter Your server IP: ")
    port = int(input("Enter Your server port: "))
    start_server(ip, port)
    

	

