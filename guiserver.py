import threading
import socket
import tkinter as tk
from tkinter import messagebox

class ServerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("\__F__A__C__R__/")

        self.ip_label = tk.Label(self.root, text="Enter server IP:")
        self.ip_label.pack()

        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.pack()

        self.port_label = tk.Label(self.root, text="Enter server port:")
        self.port_label.pack()

        self.port_entry = tk.Entry(self.root)
        self.port_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Server", command=self.start_server)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Server", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.pack()

        self.log_text = tk.Text(self.root, state=tk.DISABLED)
        self.log_text.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def start_server(self):
        ip = self.ip_entry.get()
        port = int(self.port_entry.get())

        self.server_thread = threading.Thread(target=self.run_server, args=(ip, port))
        self.server_thread.daemon = True
        self.server_thread.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def run_server(self, ip, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(10)
        self.log("Server started at {}:{}".format(ip, port))

        self.clients = []
        while True:
            client_socket, address = self.server_socket.accept()
            self.log("Accepted connection from {}".format(address))
            client_socket.send("Welcome to the chat server!".encode())
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, self.clients))
            client_thread.start()

    def handle_client(self, client_socket, clients):
        username = client_socket.recv(1024).decode()
        self.broadcast(clients, username + " has joined the chat!", client_socket)
        while True:
            message = client_socket.recv(1024).decode()
            if message == "exit":
                self.broadcast(clients, username + " has left the chat!", client_socket)
                client_socket.send("Goodbye!".encode())
                client_socket.close()
                clients.remove(client_socket)
                break
            else:
                self.broadcast(clients, username + ": " + message, client_socket)

    def broadcast(self, clients, message, sender):
        for client_socket in clients:
            if client_socket != sender:
                client_socket.send(message.encode())

    def stop_server(self):
        for client_socket in self.clients:
            client_socket.close()

        self.server_socket.close()

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.stop_server()
            self.root.destroy()

    def log(self, message):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.configure(state=tk.DISABLED)

if __name__ == '__main__':
    server_gui = ServerGUI()
