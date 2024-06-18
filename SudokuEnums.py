import enum

class SkColor(enum.Enum):
    WHITE   = 0
    BLUE    = 1
    RED     = 2
    
class Game_Statuses(enum.Enum):
    IN_GAME    = 0
    LOST       = 1
    COMPLETED  = 2