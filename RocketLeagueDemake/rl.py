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
ORAGNE_STARTING_XY = (224, 134)

MOVE_AMOUNT = 1 # pixels

BACKGROUND_COLOR = 2


class Car:
    def __init__(self, color=None):
        self.x = 0
        self.y = 0
        self.color = color # might not need this

    def draw(self, sheet_x, sheet_y):
        pyxel.blt(self.x, self.y, 0, sheet_x, sheet_y, 32, 32, colkey=BACKGROUND_COLOR)

    def move(self, dir=None):
        # Forward and backward movement for blue
        if (dir == "f" and self.color == 0):
            self.x += MOVE_AMOUNT
        elif (dir == "b" and self.color == 0):
            self.x -= MOVE_AMOUNT

        if (dir == 'f' and self.color == 1):
            self.x -= MOVE_AMOUNT
        elif(dir == 'b' and self.color == 1):
            self.x += MOVE_AMOUNT

# TODO need to add gravity to this fool
class Ball:
    def __init__(self):
        self.x = 0
        self.y  = 0
        self.r = 0
        self.color = 7 # grey
        self.gravity = 0 # idk how I want to handle the physics

    def draw(self):
        pass


# Maybe add these to App class as member vars
# NOTE last time I tried, Pyxel wouldn't read the car vars

blue_car = Car(0)
orange_car = Car(1)

blue_car.x = BLUE_STARTING_XY[0]
blue_car.y = BLUE_STARTING_XY[1]

orange_car.x = ORAGNE_STARTING_XY[0]
orange_car.y = ORAGNE_STARTING_XY[1]


class App:
    def __init__(self, width, height):
        pyxel.init(width, height, quit_key=pyxel.KEY_ESCAPE, title="Retro Car Soccer")

        # Add sprites to virutal spritesheet
        pyxel.images[0].load(0, 0,'assets/blue_rl_car.png')
        pyxel.images[0].load(32, 0, 'assets/orange_rl_car.png')

        pyxel.run(self.update, self.draw)
        
    # Check for player input
    # Check for collisions
    # Update x, y values
    def update(self):
        if (pyxel.btn(pyxel.KEY_W)):
            blue_car.move('f')
        elif (pyxel.btn(pyxel.KEY_S)):
            blue_car.move('b')

        if (pyxel.btn(pyxel.KEY_UP)):
            orange_car.move('f')
        elif (pyxel.btn(pyxel.KEY_DOWN)):
            orange_car.move('b')

        # TODO check for collisions
        # TODO add physics lmao

    # render everything
    def draw(self):
        pyxel.cls(BACKGROUND_COLOR) # draw some tint to the background while clearing the screen

        self.draw_cars()

        self.draw_ball()

    # Draw game objects
    def draw_walls():
        pass

    def draw_ball(self):
        pyxel.circ(128, 84, 8, 7) # ball

    def draw_cars(self):
        # Draw the first car to the screen 
        blue_car.draw(0, 0) # Blue Car

        orange_car.draw(32, 0) # Orange car

# Run this SOB
App(SCREEN_WIDTH, SCREEN_HEIGHT)