class Ball:

    def __init__(self, colour: str, size: str, weight: int, ball_type: str )-> None:
        self.colour = colour
        self.size = size
        self.weight = weight
        self.ball_type = ball_type

    def bounce(self):
        if self.ball_type.lower() == "bowling":
            print("Bowling balls can't bounce!")
        else:
            print(f"The {self.ball_type} ball is bouncing!")


if __name__ == "__main__":
    ball_one = Ball('black', 6, 12, 'bowling')
    ball_two = Ball('red', 12, 1, 'beach')
    
    ball_one.bounce()
    ball_two.bounce()