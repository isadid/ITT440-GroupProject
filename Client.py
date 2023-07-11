import socket

def get_input():
    ip_address = input("Enter the server IP address: ")
    port_number = input("Enter the server port number: ")
    return ip_address, port_number

def main():
    ip_address, port_number = get_input()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.248.134", 8484))

    message = input("Enter a message to send to the server: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Server reply: {response}")

    client_socket.close()

if _name_ == "_main_":
    main()
