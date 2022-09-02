from snake_ladder.models.game import Game


def main():
    board_size = int(input("Enter board size: "))
    players_count = int(input("Enter players count: "))
    players = list(map(str, input().split()))
    dice_faces = int(input("Enter dice faces: "))

    snakes_count = int(input("Enter snakes count: "))
    snakes = []
    for i in range(snakes_count):
        snakes.append(tuple(map(int, input().split())))

    ladders_count = int(input("Enter snakes count: "))
    ladders = []
    for i in range(ladders_count):
        ladders.append(tuple(map(int, input().split())))

    snake_ladder_game = Game(dice_faces, board_size)
    snake_ladder_game.set_players(players)
    snake_ladder_game.play_game()

if __name__ == "__main__":
    main()
