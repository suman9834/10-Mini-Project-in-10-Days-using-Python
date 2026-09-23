import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")

clock = tk.Label(
    root,
    font=("Arial", 40),
    bg="black",
    fg="white"
)

clock.pack(expand=True)

def update_time():
    current_time = strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_time)

update_time()

root.mainloop()