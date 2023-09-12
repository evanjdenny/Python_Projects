"""Creating basic classes to use for HANGMAN game."""

class Display:
    """What is displayed for the user."""
    def __init__(self, text: list):
        self.text_list = text
        self.text = ''
        for item in text:
            self.text += item+'\n'

    def __call__(self):
        print(self.text)

    def update(self):
        """Updates self.text based on changes to self.text_list."""
        self.text = ''
        for item in self.text_list:
            self.text += item+'\n'

    def edit(self, new_text: str, line: int):
        """Edit a line of text in self.text_list."""
        self.text_list[line] = new_text

class Input:
    """Get user input with a prompt."""
    def __init__(self, prompt: str):
        self.input = None
        self.prompt = prompt

    def get_input(self):
        """Get user input."""
        self.input = input(self.prompt)

class AnswerKey:
    """Answer key for Hangman prompt."""
    def __init__(self, prompt: str):
        self.key = set()
        self.prompt = prompt.lower()
        for item in self.prompt:
            self.key.add(item)
        self.key = sorted(self.key)

    def display_key(self):
        """Display the answer key."""
        print(self.key)

    def display_prompt(self):
        """Display the prompt."""
        print(self.prompt)

class Color:
    """Change color of text."""    
    colors = ['\033[0m',
              '\033[30m',
              '\033[31m',
              '\033[32m',
              '\033[33m',
              '\033[34m',
              '\033[35m',
              '\033[36m',
              '\033[37m',]

    def __init__(self, text: str, color: int):
        if color >= 0 and color < 9:
            self.text = self.colors[color] + text
        else:
            self.text = self.colors[0] + text

    def display(self):
        """Displays self.text to console."""
        print(self.text)

class GuessedLetters:
    """List of correctly and incorrectly guessed letters."""
    def __init__(self, prompt: str):
        self.correct_letters = AnswerKey(prompt).key
        self.guessed_letters = set()
        self.guessed_letters_correct = set()
    
    def guess_letter(self, letter: str):
        """Guess letter and add to guessed_letters and if correct,
        add to guessed_letters_correct."""
        if len(letter) == 1:
            if letter.isalpha():
                self.guessed_letters.add(letter.lower())
                for item in self.correct_letters:
                    if letter.lower() == item:
                        self.guessed_letters_correct.add(letter.lower())
            else:
                print('Invalid input.')
        else:
            print('Invalid input. ')
 