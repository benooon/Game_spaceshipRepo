from enum import Enum

class ErrorHandler(Enum):
    ERROR_X = 'x must be an integer'
    ERROR_YR = 'y must be an integer'
    ERROR_WIDTH = 'width must be an integer'
    ERROR_HEIGHT = 'height must be an integer'
    ERROR_CAPTION = 'caption must be a string'
    ERROR_SPACESHIP1_MUST_BE_SPACESHIP = "spaceship1 must be an instance of Spaceship"
    ERROR_SPACESHIP2_MUST_BE_SPACESHIP = "spaceship2 must be an instance of Spaceship"
    ERROR_WINDOW_MUST_BE_WINDOW = "window must be an instance of Window"
    ERROR_BULLET_MUST_BE_BULLET = "bullet must be an instance of Bullet"
