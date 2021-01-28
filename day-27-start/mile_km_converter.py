from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def button_clicked():
    distance_miles = float(input.get())
    distance_km = distance_miles*1.609
    label_result.config(text=distance_km)

#labels
label_miles = Label(text="Miles", font=("Arial", 24, "normal"))
label_miles.grid(column=3, row=0)

label_km = Label(text="Km", font=("Arial", 24, "normal"))
label_km.grid(column=3, row=1)

label_is_equal = Label(text="is equal to", font=("Arial", 24, "normal"))
label_is_equal.grid(column=0, row=1)

label_result = Label(text="0", font=("Arial", 24, "normal"))
label_result.grid(column=1, row=1)

#entry
input = Entry(width=10)
input.grid(column=1, row=0)
input.focus()

#button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)








window.mainloop()