import random

def start(x, y, counts):
    field = []
    symbols = []
    symbol_count = {symbol: counts.get(symbol, 0) for symbol in ['1', '2', 'E', 'X']}

    for symbol, count in counts.items():
        if symbol in symbol_count:
            symbols.extend([symbol] * min(count, symbol_count[symbol]))

    remaining_cells = x * y - len(symbols)
    symbols.extend(['#'] * remaining_cells)

    random.shuffle(symbols)

    for i in range(y):
        row = symbols[i * x:(i + 1) * x]
        field.append(row)

    return field

def printState(field):
    for row in field:
        print("".join(row))
    print()

def calculate_next_state(current_state):
    new_state = []
    no_more_1_or_2 = True
    for i, row in enumerate(current_state):
        new_row = []
        for j, symbol in enumerate(row):
            if symbol in ['1', '2']:
                no_more_1_or_2 = False
                if 'E' in get_neighbors(current_state, i, j):
                    new_row.append(symbol)  # 1 or 2 stays if E is present in the neighborhood
                elif 'X' in get_neighbors(current_state, i, j):
                    new_row.append('#')  # 1 or 2 dies if X is present in the neighborhood
                else:
                    new_row.append(symbol)  # 1 or 2 stays if neither E nor X is present
            else:
                new_row.append(symbol)  # Other symbols remain unchanged
        new_state.append(new_row)

    printState(new_state)  # Print the state after each round
    return new_state, no_more_1_or_2

def get_neighbors(field, row_idx, col_idx):
    neighbors = []
    for i in range(row_idx - 1, row_idx + 2):
        for j in range(col_idx - 1, col_idx + 2):
            if 0 <= i < len(field) and 0 <= j < len(field[0]) and (i != row_idx or j != col_idx):
                neighbors.append(field[i][j])
    return neighbors

def main():
    counts = {'1': 3, '2': 2, 'E': 4, 'X': 1}  # Define counts for each symbol
    field = start(5, 5, counts)
    print("Initial state:")
    printState(field)
    while True:
        field, game_over = calculate_next_state(field)
        if game_over:
            print("No more 1s or 2s. Game over.")
            break

if __name__ == "__main__":
    main()
