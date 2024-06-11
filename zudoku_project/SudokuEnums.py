import enum

class SkColor(enum.Enum):
    WHITE   = 0
    BLUE    = 1
    RED     = 2
    
class Game_Statuses(enum.Enum):
    STATIS  = 0
    DEFEAT  = 1
    VICTORY = 2