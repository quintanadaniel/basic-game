import pygame.draw

from color import Color


class Player:
    def __init__(self, x, y, size, color: Color = Color.RED):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def detect_collision(self, other):

        if (self.x <= other.x < (self.x + self.size)) or (
            other.x <= self.x < (other.x + other.size)
        ):
            if (self.y <= other.y < (self.y + self.size)) or (
                other.y <= self.y < (other.y + other.size)
            ):
                return True
        return False


class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=Color.BLUE)


class LargeEnemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=100, color=Color.BLUE)


class HumanPlayer(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=Color.RED)
