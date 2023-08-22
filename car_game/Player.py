import pygame
from mapaa import Map

class Car:
    def __init__(self, x, y, map:Map):
        # Spawn do carro
        self.position = {"x":x/3,"y":y/2}
        self.road = map.get_road()

        self.car_asset = pygame.transform.scale(pygame.image.load('assets/Car.png'),(100, 100))


    def car_draw(self, display):
        display.blit(self.car_asset, (self.position["x"], self.position["y"]))

    def on_event(self, event):

        if event.key == pygame.K_a:
            if (self.position["x"] - 30) <= self.road["x_inicio"]:
                self.position["x"] = self.road["x_inicio"]
            elif (self.position["x"] - 30) >= self.road["x_fim"]:
                self.position["x"] = self.road["x_fim"]
            else:
                self.position["x"] -= 30

        elif event.key == pygame.K_d:
            self.position["x"] += 30

