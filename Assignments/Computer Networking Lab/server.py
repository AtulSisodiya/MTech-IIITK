import socket
import threading

# Game board and player setup
board = [' ' for _ in range(9)]  # 3x3 Tic-Tac-Toe board
current_player = 'X'  # X starts the game
lock = threading.Lock()  # To manage concurrent access to game state

# Function to print the current game board
def print_board():
    print(f"""
      {board[0]} | {board[1]} | {board[2]}
     ---+---+---
      {board[3]} | {board[4]} | {board[5]}
     ---+---+---
      {board[6]} | {board[7]} | {board[8]}
    """)

# Check for a win or draw
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for (x, y, z) in winning_combinations:
        if board[x] == board[y] == board[z] != ' ':
            return board[x]
    if ' ' not in board:
        return 'Draw'
    return None

# Handle client connections
def handle_client(conn, addr):
    global current_player
    conn.send("Welcome to Tic-Tac-Toe!\n".encode())
    conn.send(print_board().encode())

    while True:
        with lock:
            conn.send(f"Your turn, {current_player}. Enter position (1-9): ".encode())
            move = conn.recv(1024).decode().strip()

            if not move.isdigit() or not 1 <= int(move) <= 9:
                conn.send("Invalid move. Try again.\n".encode())
                continue

            move = int(move) - 1

            if board[move] != ' ':
                conn.send("Position already taken. Try again.\n".encode())
                continue

            board[move] = current_player
            winner = check_winner()

            if winner:
                conn.send(f"{winner} wins the game!\n".encode())
                break

            # Switch player turns
            current_player = 'O' if current_player == 'X' else 'X'

            # Update all clients
            conn.send(print_board().encode())

    conn.close()

# Server setup
def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)  # Allow up to 2 players

    print(f"Server started on {host}:{port}. Waiting for players to connect...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Player connected from {addr}.")
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
