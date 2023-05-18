import threading
import socket
import time
import tkinter as tk
import webbrowser
import random
from datetime import datetime

class ClientGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("\__F__A__C__R__/")
        self.root.configure(background='#000000')  # set the background color

        self.date_label = tk.Label(self.root, text="", bg='#000000', fg='#00FF00')
        self.date_label.pack()

        # Add a label for the animated name
        self.name_label = tk.Label(self.root, text="", bg='#000000', fg='#00FF00')
        self.name_label.pack()

        self.ip_label = tk.Label(self.root, text="Enter server IP:", bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.ip_label.pack()

        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.pack()

        self.port_label = tk.Label(self.root, text="Enter server port:", bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.port_label.pack()

        self.port_entry = tk.Entry(self.root)
        self.port_entry.pack()

        self.username_label = tk.Label(self.root, text="Enter your username:", bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.connect_button = tk.Button(self.root, text="Connect", command=self.connect_to_server, bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.connect_button.pack()

        # add a button to redirect to the website
        self.redirect_button = tk.Button(self.root, text="Connect to webchatRoom", command=self.redirect_to_website, bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.redirect_button.pack()

        # create a frame to hold the log_text and scrollbar widgets
        self.log_frame = tk.Frame(self.root)
        self.log_frame.pack()

        # create a scrollbar widget
        self.log_scrollbar = tk.Scrollbar(self.log_frame)

        # create a Text widget embedded in the scrollbar widget
        self.log_text = tk.Text(self.log_frame, yscrollcommand=self.log_scrollbar.set, state=tk.DISABLED, bg='#000000', fg='#00FF00', insertbackground='#00FF00', font=('Courier New', 11))
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # configure the scrollbar to scroll the Text widget
        self.log_scrollbar.config(command=self.log_text.yview)
        self.log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_label = tk.Label(self.root, text="Enter message:", bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.message_label.pack()

        self.message_entry = tk.Text(self.root, height=5, width=50)
        self.message_entry.pack()
        self.message_entry.bind('<Return>', self.send_message)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, state=tk.DISABLED, bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.send_button.pack()

        # Add a Clear Chat button
        self.clear_button = tk.Button(self.root, text="Clear Chat", command=self.clear_chat, bg='#000000', fg='#00FF00')  # set the background and foreground color
        self.clear_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Start the name animation
        self.animate_name()

        # Start the date update thread
        self.update_date()

        self.root.mainloop()

    def redirect_to_website(self):
        webbrowser.open("https://webchatroomv4.netlify.app/")

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
                self.log_with_typewriter_effect(message)
            except:
                break

    def send_message(self, event=None):
        message = self.message_entry.get("1.0", tk.END).strip()
        self.client_socket.send(message.encode())
        self.log(f"{self.username}: {message}")  # Add sender's message to log
        self.message_entry.delete("1.0", tk.END)

    def clear_chat(self):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state=tk.DISABLED)

    def on_closing(self):
        self.client_socket.send("exit".encode())
        self.root.destroy()

    def log(self, message):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.configure(state=tk.DISABLED)
        self.log_text.yview(tk.END)  # scroll to the bottom of the Text widget

    def log_with_typewriter_effect(self, message):
        self.log_text.configure(state=tk.NORMAL)
        for char in message:
            self.log_text.insert(tk.END, char)
            self.log_text.yview(tk.END)
            self.root.update()
            time.sleep(0.02)
        self.log_text.insert(tk.END, "\n")
        self.log_text.configure(state=tk.DISABLED)
        self.log_text.yview(tk.END)  # scroll to the bottom of the Text widget

    def generate_random_color(self):
        r = lambda: random.randint(0, 255)
        return "#" + format(r(), '02x') + format(r(), '02x') + format(r(), '02x')

    def animate_name(self):
        hacker_name = "山乇ㄥㄥ匚ㄖ爪乇"
        self.name_label.config(text="", fg=self.generate_random_color())
        for _ in range(len(hacker_name)):
            self.name_label.config(text=self.name_label.cget("text") + hacker_name[_])
            self.root.update()
            time.sleep(0.2)
        self.root.after(200, self.animate_name)

    def update_date(self):
        current_date_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
        self.date_label.config(text=current_date_time)
        self.root.after(1000, self.update_date)

if __name__ == '__main__':
    client_gui = ClientGUI()
