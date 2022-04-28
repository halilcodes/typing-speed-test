import random
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from data import quotes
import time

# start/submit buttons functionality
# make the counter a global value so bath start and submit would get the counter

start_time = 0.0
finish_time = 0.0


def start():
    global start_time 
    start_time = time.perf_counter()
    return start_time

def submit():
    global start_time
    if type_entry.get() == quote_itself:
        finish_time = time.perf_counter()
        time_passed = finish_time - start_time
        messagebox.showinfo(title="Well Done! ", message=f"Time Passed: {time_passed:.3}")
    else:
        messagebox.showinfo(title="Booo", message="you didn't write correctly. Fast but bad does not count!")


# ----- UI SETUP ------

window = Tk()
window.title("Typing Speed Test by Halil Hasmer")
window.config(padx=50, pady=50)

# Logo Size Setup
logo = Image.open("watermark_black_halil.png")
logo = logo.resize((150,50), Image.ANTIALIAS)

# Logo Insert
canvas = Canvas(height=60, width=200, bg="red")
logo_img = ImageTk.PhotoImage(logo)
canvas.create_image(100, 30, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# Choose text to write
quote = random.choice(quotes)
quote_itself = quote["quote"]
quote_source = quote["source"]

# Show quote on GUI
quote_label = Label(text=quote_itself)
quote_label.grid(row=1, column=0, sticky="w", columnspan=2)

# Entry box for user to type in
type_entry = Entry(width=100)
type_entry.grid(row=2, column=0, columnspan=2)

# add start/submit button
start_button = Button(text="Start", command=start)
start_button.grid(row=3, column=0)
submit_button = Button(text="Submit Result", command=submit)
submit_button.grid(row=3, column=1)

window.mainloop()