from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = None
# -------------------------read csv data-------------------------
try:
    french_words_dataframe = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    french_words_dataframe = pandas.read_csv("data/french_words.csv")

french_words_dict = french_words_dataframe.to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    current_card = random.choice(french_words_dict)
    display_word = (current_card["French"])
    canvas.itemconfig(idiom_text, text=f"French", fill="black")
    canvas.itemconfig(word_text, text=f"{display_word}", fill="black")
    flip_timer = window.after(3000, flip_card)


# -------------------------flipping the card-------------------------
def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    display_word = (current_card["English"])
    canvas.itemconfig(word_text, text=f"{display_word}", fill="white")
    canvas.itemconfig(idiom_text, text=f"English", fill="white")


def is_known():
    french_words_dict.remove(current_card)
    data = pandas.DataFrame(french_words_dict)
    data.to_csv("data/to_learn.csv", index=False)
    next_card()
# -------------------------UI-------------------------


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 262, image=card_front)
idiom_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=is_known, highlightthickness=0)
right_button.grid(column=1, row=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
