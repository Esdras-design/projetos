import numpy as np

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if np.all(board[i, :] == 'X') or np.all(board[:, i] == 'X'):
            return 'X'
        if np.all(board[i, :] == 'O') or np.all(board[:, i] == 'O'):
            return 'O'
    
    if board[0, 0] == board[1, 1] == board[2, 2] and board[0, 0] != ' ':
        return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] and board[0, 2] != ' ':
        return board[0, 2]
    
    return None

def is_full(board):
    return not np.any(board == ' ')

def main():
    board = np.full((3, 3), ' ')
    current_player = 'X'
    
    while True:
        print_board(board)
        row = int(input(f"Jogador {current_player}, escolha a linha (0-2): "))
        col = int(input(f"Jogador {current_player}, escolha a coluna (0-2): "))
        
        if board[row, col] == ' ':
            board[row, col] = current_player
        else:
            print("Essa posição já está ocupada! Tente novamente.")
            continue
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Jogador {winner} venceu!")
            break
        
        if is_full(board):
            print_board(board)
            print("Empate!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()