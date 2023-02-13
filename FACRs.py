'Chat Room Connection - Client-To-Client'
mport threading
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

def start_client(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    print("Connected to", ip, ":", port)
    print(client_socket.recv(1024).decode())
    username = input("Enter your username: ")
    client_socket.send(username.encode())
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()
    send_message(client_socket)

def receive_message(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(message)

def send_message(client_socket):
    while True:
        message = input()
        if message == "exit":
            client_socket.send(message.encode())
            break
        client_socket.send(message.encode())

if __name__ == '__main__':
    ip = input("Enter server IP: ")
    port = int(input("Enter server port: "))
    start_client(ip, port)
    

