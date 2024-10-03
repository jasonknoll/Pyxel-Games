import pyxel

"""
 For my very first "demake", I'm trying to 
 target Rocket League, mainly sideswipe and it's
 2D style of play.

 I'd love to build this on both Pico and here in
 Pyxel. We'll see how I do!
"""

# Constants

SCREEN_HEIGHT = 168
SCREEN_WIDTH = 256

BLUE_STARTING_XY = (0, 134)

MOVE_AMOUNT = 1


class Car:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, sheet_x, sheet_y):
        pyxel.blt(self.x, self.y, 0, sheet_x, sheet_y, 32, 32, colkey=2)

    def move(self, dir=None):
        # Forward and backward movement
        if (dir=="f"):
            self.x += MOVE_AMOUNT
        elif (dir == "b"):
            self.x -= MOVE_AMOUNT



# Maybe add these to App class as member vars

blue_car = Car()
orange_car = Car()

blue_car.x = BLUE_STARTING_XY[0]
blue_car.y = BLUE_STARTING_XY[1]

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
        if (pyxel.btn(pyxel.KEY_W)):
            blue_car.move('f')
        elif (pyxel.btn(pyxel.KEY_S)):
            blue_car.move('b')

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