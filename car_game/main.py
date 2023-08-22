import pygame
from Player import Car
from mapaa import Map

class game():
    def __init__(self, x, y):
        pygame.init()
        self.display = pygame.display.set_mode((x, y))
        self.is_game_on = True
        self.x = x
        self.y = y
        self.map = Map(x, y)
        self.car = Car(x, y, self.map)



    def loop(self):
        while self.is_game_on:
            self.display.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_game_on
                else:
                    if event.type == pygame.KEYDOWN:
                        self.car.on_event(event)


            self.map.draw_map(self.display)
            self.car.car_draw(self.display)

            pygame.display.update()

if __name__ == "__main__":
    print("Iniciando")
    joguinho = game(900,600)
    joguinho.loop()