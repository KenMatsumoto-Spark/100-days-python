from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.pack(side="left")
my_label["text"] = "new Text"
my_label.config(text="Newer Text")
my_label.grid(column=0, row=0)

#button

def button_clicked():
    new_text = input.get()
    print("I got clicked")
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="Click Me 2", command=button_clicked)
new_button.grid(column=3, row=0)
#Entry

input = Entry(width=10)
input.grid(column=4, row=3)





window.mainloop()