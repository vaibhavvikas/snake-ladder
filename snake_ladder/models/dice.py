import random


class Dice:

    def __init__(self, faces):
        self.faces = faces

    def get_random_face(self):
        score = 0
        moves = 0

        while True:
            dice_score = random.randint(1, self.faces)
            moves += 1

            if dice_score != self.faces:    
                return score + dice_score

            if moves == 3:
                return 0

            score += dice_score
                