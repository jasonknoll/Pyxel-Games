import pyxel

"""
 For my very first "demake", I'm trying to 
 target Rocket League, mainly sideswipe and it's
 2D style of play.

 I'd love to build this on both Pico and here in
 Pyxel. We'll see how I do!
"""

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, sheet_x, sheet_y):
        pyxel.blt(self.x, self.y, 0, sheet_x, sheet_y, 32, 32, colkey=2)

    def move(self):
        pass


SCREEN_HEIGHT = 168
SCREEN_WIDTH = 256

blue_car = Car()
orange_car = Car()

orange_car.x = 64
orange_car.y = 64


class App:
    def __init__(self, width, height):
        pyxel.init(width, height, quit_key=pyxel.KEY_ESCAPE, title="Retro Car Soccer")
        pyxel.images[0].load(0, 0,'assets/blue_rl_car.png', incl_colors=False)
        pyxel.images[0].load(32, 32, 'assets/orange_rl_car.png', incl_colors=False)
        pyxel.run(self.update, self.draw)
        
    # Check for player input
    # Check for collisions
    # Update x, y values
    def update(self):
        pass

    # render everything
    def draw(self):
        pyxel.cls(2) # draw some tint to the background while clearing the screen

        self.draw_cars()

    # Draw game objects
    def draw_walls():
        pass

    def draw_ball():
        pass

    def draw_cars(self):
        # Draw the first car to the screen 
        blue_car.draw(0, 0) # Blue Car

        orange_car.draw(32, 32) # Orange car

# Run this SOB
App(SCREEN_WIDTH, SCREEN_HEIGHT)