import socket

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

try:
    # Query the list of applications and associated commands
    applications = eval(client_socket.recv(1024).decode())
    print('Available applications and commands:', applications)

    while True:
        command = input('Enter command (or "exit" to quit): ')
        if command.lower() == 'exit':
            break
        client_socket.send(command.encode())
        result = client_socket.recv(1024).decode()
        print('Result:', result)
        
except socket.error as e:
    print(f'Socket error: {e}')
except Exception as e:
    print(f'Unexpected error: {e}')
finally:
    client_socket.close()