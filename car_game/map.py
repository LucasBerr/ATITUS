import keyboard

class map:
    def __init__(self):
        self.streetLeft =   "\t\t\tx"
        self.streetMiddle = "|"
        self.streetRight =  "x"
        self.blanckSpaces = "  "

        self.interact = ["  ", "🚗", "🚙"] 
        
        # x       |   🚗  x

        self.window = 10

    def construct_street(self):
        for i in range(self.window):
             print(self.streetLeft + self.interact[0] + self.interact[0] + self.streetMiddle + self.interact[0] + self.interact[0] + self.streetRight)

    def construct_street_with_player(self):
            print(self.streetLeft + self.interact[0] + self.interact[1] + self.streetMiddle + self.interact[0] + self.interact[0] + self.streetRight)

# 


mapa = map()
mapa.construct_street()
mapa.construct_street_with_player()