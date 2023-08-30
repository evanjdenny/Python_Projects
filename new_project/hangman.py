from text import h0, h1, h2, h3, h4, h5, h6, guess_prompt
from main_menu import Menu

def check_letters(user_input):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    punctuation = [' ', '\'', ',', '.', '?', '!', '@', '#', '$', '%', '&', '*', '(', ')', '"', '=', '+', '-']
    for item in letters:
        if user_input == item:
            return '_ '
    for item in numbers:
        if user_input == item:
            return item
    for item in punctuation:
        if user_input == item:
            return item

class Hangman_Session:
    lives = 6
    answer_key = []
    prompt = ''
    prompt_answer = ''

    def __init__(self, prompt: str):
        self.prompt_answer = prompt
        for item in prompt:
            self.prompt += check_letters(item)
        self.start_menu = Menu(h0, True, hangman_prompt=self.prompt, user_input_prompt=guess_prompt)
        self.h1_menu = Menu(h1, True, hangman_prompt=self.prompt, user_input_prompt=guess_prompt)
        self.h2_menu = Menu(h2, True, hangman_prompt=self.prompt, user_input_prompt=guess_prompt)
        self.h3_menu = Menu(h3, True, hangman_prompt=self.prompt, user_input_prompt=guess_prompt)
        self.h4_menu = Menu(h4, True, hangman_prompt=self.prompt, user_input_prompt=guess_prompt)
        self.h5_menu = Menu(h5, True, hangman_prompt=self.prompt, user_input_prompt=guess_prompt)
        self.end_menu = Menu(h6, True, hangman_prompt=self.prompt, user_input_prompt="GAME OVER! PLAY AGAIN? (y/n): ")

    def play(self):
        while self.lives is 6:
            self.user_input = self.start_menu.display()