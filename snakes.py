class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    def __init__(self, color):
        self.color = color
    
    def bite(self, other):
        """Deliver a dose of venom."""
        pass

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        """some changes in squeeze function"""
    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    pass
