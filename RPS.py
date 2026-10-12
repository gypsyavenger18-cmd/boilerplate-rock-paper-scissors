def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    # Track n-gram patterns across matches
    if not hasattr(player, "patterns"):
        player.patterns = {}

    # Reset learned patterns between new bots/matches
    if len(opponent_history) <= 1:
        player.patterns.clear()

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    n = 4  # Looks at sequences of the previous 4 moves

    if len(opponent_history) >= n:
        pattern = "".join(opponent_history[-n:])
        player.patterns[pattern] = player.patterns.get(pattern, 0) + 1

    # Default move
    guess = "R"

    if len(opponent_history) >= n - 1:
        recent = "".join(opponent_history[-(n - 1):])
        potential_plays = [recent + move for move in ["R", "P", "S"]]

        # Predict the opponent's next move based on historical transition frequencies
        predicted_move = max(
            ["R", "P", "S"],
            key=lambda move: player.patterns.get(recent + move, 0)
        )
        guess = ideal_response[predicted_move]

    return guess