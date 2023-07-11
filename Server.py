import socket
import datetime
import multiprocessing

# Function to handle client requests
def handle_client(client_socket, client_address):
    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print('Received message from client:', data)

        # Get the current date and time
        current_datetime = datetime.datetime.now().strftime('%d %B %Y, %H:%M')

        # Create the combined string with the current date and time
        combined_string = '{} - {}'.format(data, current_datetime)

        # Send the combined string back to the client
        client_socket.sendall(combined_string.encode())
        print('Combined string sent to client:', combined_string)
    except Exception as e:
        print('Error occurred during communication:', str(e))

    # Close the connection with the client
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('192.168.248.134', 8484)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections (max 5 connections in the queue)
server_socket.listen(5)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a client to connect...')
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Client connected:', client_address)
    

# Create a new process to handle the client request
process = multiprocessing.Process(target=handle_client, args=(client_socket, client_address))
    process.start()
