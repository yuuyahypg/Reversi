import ai

class Human():
    """
    human class

    Members:

        color   --human's color(black or white)
    """
    def __init__(self, color="black"):
        self.color = color

class Computer():
    """
    computer class

    Members:

        color   --computer's color(black or white)
        ai      --ai module (select the best position to put)
    """
    def __init__(self, color="white"):
        self.color = color
        self.ai = ai.Ai()
