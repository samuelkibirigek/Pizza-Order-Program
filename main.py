from tkinter import *

window = Tk()
window.title("Place Your Order Now!")
window.config(padx=50, pady=50)

comm = "Welcome to Python Pizza Deliveries!"
canvas = Canvas(height=60, width=300, bg="Green")
canvas.grid(row=0, column=0, columnspan=2)

focus = Label(text=f"{comm}", font=("Ariel", 13, "bold"), bg="green")
focus.place(x=23, y=25)
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


def price():
    pizza_size = size_entry.get().upper()
    pizza_add_pepperoni = add_pepperoni_entry.get().upper()
    pizza_extra_cheese = extra_cheese_entry.get().upper()

    size_pizza = 0
    pepperoni = 0
    cheese = 0

    if pizza_size == "S":
        size_pizza = 15
    elif pizza_size == "M":
        size_pizza = 20
    elif pizza_size == "L":
        size_pizza = 25

    if pizza_add_pepperoni == "Y" and (pizza_size == "M" or pizza_size == "L"):
        pepperoni = 3
    elif pizza_add_pepperoni == "Y":
        pepperoni = 2
    elif pizza_add_pepperoni == "N":
        pepperoni = 0

    if pizza_extra_cheese == "Y":
        cheese = 1
    elif pizza_extra_cheese == "N":
        cheese = 0

    total = size_pizza + pepperoni + cheese
    focus.config(text=f"PAY ${total}")


order = Button(text="Order", command=price)
order.grid(row=4, column=0, columnspan=2)
order.config(bg="green")

window.mainloop()
