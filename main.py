from tkinter import *

window = Tk()
window.title("Place Your Order Now!")
window.config(padx=50, pady=50)

comm = "Welcome to Python Pizza Deliveries!"
canvas = Canvas(height=60, width=300, bg="Green")
canvas.create_text(150, 30, text=f"{comm}", font=("Ariel", 13, "bold"))
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



size = size_entry.get()
add_pepperoni = add_pepperoni_entry.get()
extra_cheese = extra_cheese_entry.get()
size_pizza = 0
pepperoni = 0
cheese = 0

if size == "S":
    size_pizza = 15
elif size == "M":
    size_pizza = 20
elif size == "L":
    size_pizza = 25

if add_pepperoni == "Y" and size == "M" or size == "L":
    pepperoni = 3
elif add_pepperoni == "Y":
    pepperoni = 2
elif add_pepperoni == "N":
    pepperoni = 0

if extra_cheese == "Y":
    cheese = 1
elif extra_cheese == "N":
    cheese = 0


def price():
    total = size_pizza + pepperoni + cheese
    payment = f"${total}"
    canvas.create_text(150, 50, text=f"{payment}", font=("Ariel", 13, "bold"))


order = Button(text="Order", command=price)
order.grid(row=4, column=0, columnspan=2)
order.config(bg="green")

window.mainloop()
