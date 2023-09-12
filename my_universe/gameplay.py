class History:
    """History of actions and responses from Engine."""
    history = []

    def add_item(self, item: str):
        self.history.append(item)

    def print_history(self):
        x = 5
        if len(self.history) < 5:
            x = len(self.history)
            y = 5-x
            while y>0:
                print()
                y-=1
        while x>0:
            print(self.history[-x])
            x-=1

class Engine:
    """Read, Eval, Print, Loop (REPL)"""
    __player = None
    __history = History()
    __tile = None
    __zone = None

    def set_player(self, player):
        self.__player = player

    def get_player(self):
        return self.__player

    def new_history(self, history):
        self.__history = History()

    def add_item_to_history(self, item):
        self.__history.add_item(item)

    def print_history(self):
        self.__history.print_history()

    def set_tile(self, tile):
        self.__tile = tile

    def get_tile(self):
        return self.__tile
    
    def set_zone(self, zone):
        self.__zone = zone

    def get_zone(self):
        return self.__zone


    def repl(self):
        """Game loop"""

class UserInput:
    """User Input"""
    raw_user_input = ''
    action = None
    target = None
    optional = None

    def get_input(self):
        """Gets input from the user."""
        self.raw_user_input = input('> ')

