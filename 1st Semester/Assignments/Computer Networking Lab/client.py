import socket

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server.")

    while True:
        # Receive data from server
        server_message = client_socket.recv(1024).decode()
        print(server_message)

        # If the server requests a move, input the player's move
        if "Your turn" in server_message:
            move = input("Enter your move (1-9): ")
            client_socket.send(move.encode())

        # End game condition
        if "wins the game" in server_message or "Draw" in server_message:
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
