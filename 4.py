def minimax(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or isinstance(node, int):
        return node
    if maximizing_player:
        best = float('-inf')
        for child in node:
            value = minimax(child, depth - 1, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for child in node:
            value = minimax(child, depth - 1, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

game_tree = [
    [8, 6],       # Route A
    [4, 10]       # Route B
]
best_score = float('-inf')
best_route = None
for i, route in enumerate(game_tree):
    score = minimax(
        route,
        depth=1,
        alpha=float('-inf'),
        beta=float('inf'),
        maximizing_player=True
    )
    print("Route", chr(65 + i), "Score:", score)
    if score > best_score:
        best_score = score
        best_route = chr(65 + i)

print("\nBest Route:", best_route)
print("Best Score:", best_score)
