def player_move(player, dice_face, initial_pos, final_pos):
    if initial_pos != final_pos:
        return f"{player} rolled a {dice_face} and moved from {initial_pos} to {final_pos}"
    return f"{player} rolled a {dice_face} and but can't move from {initial_pos}"
