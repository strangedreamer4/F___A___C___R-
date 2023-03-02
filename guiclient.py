import threading
import socket
import tkinter as tk

class ClientGUI:
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

        self.username_label = tk.Label(self.root, text="Enter your username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.connect_button = tk.Button(self.root, text="Connect", command=self.connect_to_server)
        self.connect_button.pack()

        # create a frame to hold the log_text and scrollbar widgets
        self.log_frame = tk.Frame(self.root)
        self.log_frame.pack()

        # create a scrollbar widget
        self.log_scrollbar = tk.Scrollbar(self.log_frame)

        # create a Text widget embedded in the scrollbar widget
        self.log_text = tk.Text(self.log_frame, yscrollcommand=self.log_scrollbar.set, state=tk.DISABLED)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # configure the scrollbar to scroll the Text widget
        self.log_scrollbar.config(command=self.log_text.yview)
        self.log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_label = tk.Label(self.root, text="Enter message:")
        self.message_label.pack()

        self.message_entry = tk.Entry(self.root)
        self.message_entry.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, state=tk.DISABLED)
        self.send_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def connect_to_server(self):
        ip = self.ip_entry.get()
        port = int(self.port_entry.get())
        self.username = self.username_entry.get()

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip, port))
        self.client_socket.send(self.username.encode())

        self.connect_button.config(state=tk.DISABLED)
        self.send_button.config(state=tk.NORMAL)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                self.log(message)
            except:
                break

    def send_message(self):
        message = self.message_entry.get()
        self.client_socket.send(message.encode())
        self.message_entry.delete(0, tk.END)

    def on_closing(self):
        self.client_socket.send("exit".encode())
        self.root.destroy()

    def log(self, message):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.configure(state=tk.DISABLED)
        self.log_text.yview(tk.END)  # scroll to the bottom of the Text widget

if __name__ == '__main__':
    client_gui = ClientGUI()
