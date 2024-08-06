import tkinter as tk

class HangmanGame:
    def __init__(self):
        self.word = "secret"
        self.guesses = ""
        self.turns = 10

        self.window = tk.Tk()
        self.window.title("Hangman Game")

        self.output_label = tk.Label(self.window, text="Hello! Welcome to Hangman Game", wraplength=400)
        self.output_label.pack()

        self.name_label = tk.Label(self.window, text="What is your name?")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_name)
        self.submit_button.pack()

        self.window.mainloop()

    def submit_name(self):
        self.name = self.name_entry.get()
        self.name_entry.delete(0, tk.END)
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.submit_button.pack_forget()
        self.output_label['text'] = "Hello, " + self.name + "! Guess the word!"
        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.pack()
        self.guess_button = tk.Button(self.window, text="Guess", command=self.submit_guess)
        self.guess_button.pack()

    def submit_guess(self):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)
        self.guesses += guess
        failed = 0
        output = ""
        for char in self.word:
            if char in self.guesses:
                output += char + " "
            else:
                output += "_ "
                failed += 1
        self.output_label['text'] = output
        if failed == 0:
            self.output_label['text'] = "You won!"
        elif guess not in self.word:
            self.turns -= 1
            self.output_label['text'] += "\nWrong! You have " + str(self.turns) + " more guesses."
            if self.turns == 0:
                self.output_label['text'] = "You Lose!"

HangmanGame()