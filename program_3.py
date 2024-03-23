# program 3
# Input Information and print in a fancy way
import pyfiglet
import shutil
import time
# Add tkinter to the program
import tkinter as tk
from tkinter import font
# Create Main window and Add labels
window = tk.Tk()
window.config(bg="darkseagreen")
window.title("Personal Informations")
name_label=tk.Label(window, text="What is you name?",
font=font.Font(family="Consolas",size=17), bg="seagreen", fg="white")
name_label.grid(row=0, column=0, padx=15, pady=15)
age_label=tk.Label(window, text="How old are you?",
font=font.Font(family="Consolas", size=17), bg="seagreen", fg="white")
age_label.grid(row=1, column=0, padx=15, pady=15)
hobby_label=tk.Label(window, text="What is your hobby?",
font=font.Font(family="Consolas", size=17), bg="seagreen", fg="white")
hobby_label.grid(row=2, column=0, padx=15, pady=15)
dream_label=tk.Label(window, text="Dream travel destination?",
font=font.Font(family="Consolas", size=17), bg="seagreen", fg="white")
dream_label.grid(row=3, column=0, padx=15, pady=15)
# Add Input to the window
name_entry=tk.Entry(window, font=font.Font(family="Consolas", size=15))
name_entry.grid(row=0, column=1, padx=15, pady=15)
age_entry=tk.Entry(window, font=font.Font(family="Consolas", size=15))
age_entry.grid(row=1, column=1, padx=15, pady=15)
hobby_entry=tk.Entry(window, font=font.Font(family="Consolas", size=15))
hobby_entry.grid(row=2, column=1, padx=15, pady=15)
dream_entry=tk.Entry(window, font=font.Font(family="Consolas", size=15))
dream_entry.grid(row=3, column=1, padx=15, pady=15)
# Add fancy way to print
def print_information():
    name = name_entry.get()
    age = age_entry.get()
    hobby = hobby_entry.get()
    dream = dream_entry.get()
    text = pyfiglet.figlet_format(f"Hello {name} !!!\nAge : {age}\nYou love {hobby}\nYou'd like to visit {dream}")
    final_text = (f"\033[38;5;157m{text}\033[0m")
    for char in final_text:
        print(char, end="", flush=True)
        time.sleep(0.008)
    window.destroy()
# Add print button and finish up the program
print_button = tk.Button(window, text="Print Information",
font=font.Font(family="Consolas", size=17),
bg="seagreen", fg="white",
command=print_information)
print_button.grid(row=4, column=0, columnspan=2, padx=15, pady=15)

window.mainloop()