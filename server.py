import osascript
import socket
import json

applications = {
    'music': {
        'open': 'tell application "Music" to activate',
        'play': 'tell application "Music" to play',
        'pause': 'tell application "Music" to pause',
        'next': 'tell application "Music" to next track',
        'previous': 'tell application "Music" to previous track',
        'close': 'tell application "Music" to quit'
    },
    'terminal': {
        'open': 'tell application "Terminal" to activate',
        'new_tab': 'tell application "Terminal" to do script ""',
        'close': 'tell application "Terminal" to quit'
    }
}
app_commands = {app: list(commands.keys()) for app, commands in applications.items()}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print('Server is listening on port 12345')

def handle_client_connection(server_socket, applications, app_commands):
    client_socket, client_address = None, None
    try:
        # Accept connections from clients
        client_socket, client_address = server_socket.accept()
        print(f'Connected by {client_address}')

        # Send the list of applications and available commands to the client
        client_socket.send(json.dumps(app_commands, indent=4).encode())

        while True:
            # Execute commands received from the client and send the "results" back to the client
            command = client_socket.recv(1024).decode()
            if not command:
                break
            try:
                app, action = command.split()
                if app in applications and action in applications[app]:
                    code, out, err = osascript.run(applications[app][action])
                    print(f'Command {command} processed with output: {out}')  
                    if not out:
                        out = f'Command {command} executed successfully.'
                client_socket.send(out.encode())
            except Exception as e:
                print(f'Error processing command {command}: {e}')  
                client_socket.send(str(e).encode())
    finally:
        if client_socket:
            client_socket.close()

while True:
    handle_client_connection(server_socket, applications, app_commands)