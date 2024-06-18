import enum

class SkColor(enum.Enum):

    # Cells colors
    WHITE         = (255, 255, 255)  # White, for clear cells,
    FOCUS_BLUE    = (173, 216, 230)  # Light Blue, for focused cell
    CROSS_BLUE    = (240, 248, 255)  # Alice Blue, for highlight
    RED           = (255, 200, 200)  # R
    
    # Numbers colors
    BLACK         = (0,0,0)
    WRONG_RED     = (255, 99, 71)   # Tomato Red, for wrong nmbers
    CORRECT_BLUE  = (70, 130, 180)   # Steel Blue, for right numbers
    
    
    # WIDGETS COLOR
    WINNING_GREEN = (0, 128, 0) 
    LOSING_RED    = (128, 0, 0)

    EASY_GREEN    = (193, 255, 193)   #  pastel green
    MEDIUM_ORANGE = (255, 187, 119)  #  pastel orange
    HARD_RED      = (191, 97, 97)     #  pastel red 

    
    BACKGROUND    = (211, 211, 211)   # Light_gray
    
    # Convertor for using in setStyleSheet (QColor doesn't need meanwhile)
    def rgb_to_hex(self):
        return '#{:02x}{:02x}{:02x}'.format(self.value[0], self.value[1], self.value[2])

    def to_rgb_tuple(self):
        return self.value

    
class Game_Statuses(enum.Enum):
    IN_GAME    = 0
    LOST       = 1
    COMPLETED  = 2