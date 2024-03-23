# program 3
# Input Information and print in a fancy way

# Add tkinter to the program
import tkinter as tk
from tkinter import font
# Create Main window and Add labels
window = tk.Tk()
window.title("Personal Informations")
name_label=tk.Label(window, text="What is you name?",
font=font.Font(family="Consolas",size=17))
name_label.grid(row=0, column=0, padx=15, pady=15)
age_label=tk.Label(window, text="How old are you?",
font=font.Font(family="Consolas", size=17))
age_label.grid(row=1, column=0, padx=15, pady=15)
hobby_label=tk.Label(window, text="What is your hobby?",
font=font.Font(family="Consolas", size=17))
hobby_label.grid(row=2, column=0, padx=15, pady=15)
dream_label=tk.Label(window, text="What is your dream travel destination?",
font=font.Font(family="Consolas", size=17))
dream_label.grid(row=3, column=0, padx=15, pady=15)
# Add Input to the window
name_entry=tk.Entry(window, font=font.Font(family="Consolas", size=15))
name_entry.grid(row=0, column=1, padx=15, pady=15)
age_entry=tk.Entry(window, font=font.Font(family="Consolas", size=15))
age_entry.grid(row=1, column=1, padx=15, pady=15)
hobby_entry=tk.Entry(window, font=font.Font(famil="Consolas", size=15))
hobby_entry.grid(row=2, column=1, padx=15, pady=15)
dream_entry=tk.Entry(window, font=font.Font(family="Consolas", size=15))
dream_entry.grid(row=3, column=1, padx=15, pady=15)
# Add fancy way to print
# Add print button and finish up the program