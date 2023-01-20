from tkinter import *

window = Tk()
window.title("Place Your Order Now!")
window.config(padx=50, pady=50)

canvas = Canvas(height=60, width=300, bg="Green")
canvas.create_text(150, 30, text="Welcome to Python Pizza Deliveries!", font=("Ariel", 13, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

size = Label(text="What size pizza do you want? S, M or L? ")
size.grid(row=1, column=0)
add_pepperoni = Label(text="Do you want pepperoni? Y or N ")
add_pepperoni.grid(row=2, column=0)
extra_cheese = Label(text="Do you want extra cheese? Y or N ")
extra_cheese.grid(row=3, column=0)

size_entry = Entry()
size_entry.grid(row=1, column=1)
add_pepperoni_entry = Entry()
add_pepperoni_entry.grid(row=2, column=1)
extra_cheese_entry = Entry()
extra_cheese_entry.grid(row=3, column=1)

order = Button(text="Order")
order.grid(row=4, column=0, columnspan=2)
order.config(bg="green")
# print()
# size = input("What size pizza do you want? S, M or L? ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")


window.mainloop()
