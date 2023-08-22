import pygame

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_map(self, display):
        # Rua principal
        pygame.draw.rect(display, (66, 66, 66), (self.x/3, 0, self.x / 3, self.y))

    def get_road(self):
        return {"x_inicio":self.x/3, "y_inicio": 0, "x_fim":self.x/3, "y_fim":self.y}


