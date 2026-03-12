# Alpha-Beta Pruning Example

def alpha_beta_pruning(game_value):
    alpha_value = -1000
    beta_value = 1000

    for current_value in game_value:
        if current_value > alpha_value:
            alpha_value = current_value

        if alpha_value >= beta_value:
            break

    return alpha_value


# Game values
game_value = [3, 5, 6, 9, 1, 2]

# Find best move
best_move_value = alpha_beta_pruning(game_value)

print("Best move value:", best_move_value)