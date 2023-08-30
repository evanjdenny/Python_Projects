class Menu:
    def __init__(self, lines: list, get_user_input: bool, user_input_prompt: str = None, ):
        self.lines = lines
        self.get_user_input = get_user_input
        if self.get_user_input:
            self.user_input = ''
            if user_input_prompt is None:
                self.user_input_prompt = '> '
            else:
                self.user_input_prompt = user_input_prompt
    
    def __call__(self):
        self.display()
    
    def display(self):
        """Displays menu lines and asks user for input if required. If required, returns the user's input."""
        for item in self.lines:
            print(item)
        if self.get_user_input:
            self.user_input = input(self.user_input_prompt)
            return self.user_input

mm_text = ["HANGMAN",
           "1. PLAY",
           "2. QUIT"]

main_menu = Menu(mm_text, True)