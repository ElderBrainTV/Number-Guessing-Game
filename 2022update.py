import tkinter as tk
import random

window = tk.Tk()
window.title("Guessing Game")
window.resizable(0, 0)
window.configure(background="#1f1f1f")

frame = tk.Frame(master=window, bg="white")
frame.pack(pady=20, padx=10)

game_label = tk.Label(master=frame, 
                      text="Think of a number between 1 and 100. I'll try to guess it!", 
                      bg="white", 
                      font="Arial 18 bold")
game_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

response_label = tk.Label(master=frame, 
                         text="", 
                         bg="white", 
                         font="Arial 18 bold")
response_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

guess_label = tk.Label(master=frame, 
                       text="My guess is...", 
                       bg="white", 
                       font="Arial 18 bold")
guess_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

low = 1
high = 100

guess = 50

def update_response_label(text):
    response_label.configure(text=text)

def update_guess_label(text):
    guess_label.configure(text=text)

def get_user_range():
    global low, high
    low = int(range_entry_low.get())
    high = int(range_entry_high.get())
    update_guess_label("My guess is {}".format(random.randint(low, high)))

button_frame = tk.Frame(master=frame, bg="white")
button_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

higher_button = tk.Button(master=button_frame, 
                         text="Higher", 
                         bg="#17a2b8", 
                         font="Arial 14 bold",
                         command=lambda: higher())
higher_button.grid(row=0, column=0, padx=10, pady=10)

lower_button = tk.Button(master=button_frame, 
                         text="Lower", 
                         bg="#17a2b8", 
                         font="Arial 14 bold", 
                         command=lambda: lower())
lower_button.grid(row=0, column=1, padx=10, pady=10)

correct_button = tk.Button(master=button_frame, 
                           text="Correct", 
                           bg="#17a2b8", 
                           font="Arial 14 bold", 
                           command=lambda: correct())
correct_button.grid(row=0, column=2, padx=10, pady=10)

range_entry_frame = tk.Frame(master=frame, bg="white")
range_entry_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

range_entry_label = tk.Label(master=range_entry_frame, 
                             text="Enter a range: ", 
                             bg="white", 
                             font="Arial 14 bold")
range_entry_label.grid(row=0, column=0, padx=10, pady=10)

range_entry_low = tk.Entry(master=range_entry_frame, width=5)
range_entry_low.grid(row=0, column=1, padx=10, pady=10)

range_entry_high = tk.Entry(master=range_entry_frame, width=5)
range_entry_high.grid(row=0, column=2, padx=10, pady=10)

range_entry_button = tk.Button(master=range_entry_frame, 
                               text="Go", 
                               bg="#17a2b8", 
                               font="Arial 14 bold", 
                               command=lambda: get_user_range())
range_entry_button.grid(row=0, column=3, padx=10, pady=10)

reset_button = tk.Button(master=frame, 
                        text="Reset", 
                        bg="#17a2b8", 
                        font="Arial 14 bold", 
                        command=lambda: reset())
reset_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

def reset():
    global low, high, guess
    low = 1
    high = 100
    guess = 50
    update_guess_label("My guess is {}".format(guess))
    update_response_label("")

def higher():
    global low, high, guess
    low = guess + 1
    guess = random.randint(low, high)
    update_guess_label("My guess is {}".format(guess))

def lower():
    global low, high, guess
    high = guess - 1
    guess = random.randint(low, high)
    update_guess_label("My guess is {}".format(guess))

def correct():
    update_guess_label("I guessed it!")
    update_response_label("Yay, I guessed it!")

window.mainloop()
