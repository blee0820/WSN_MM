
class mapNode:
    def __init__(self):
        self.types = -1
        #0 = no wall
        #1 = wall

        #options only matter if type=0
        self.options = 0
        #0 = no mouse has been there
        #1 = a mouse has been there
        #2 = a mouse has been there, no more paths
