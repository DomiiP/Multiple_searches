# Testing out Python GUI with Tkinter
import tkinter as tk
from tkinter import ttk
import webbrowser
# This one is to see progress bar
import time

window = tk.Tk()
# Checkbox values
check_val = [tk.IntVar(),tk.IntVar(),tk.IntVar()]
# Progress bar value
progressBar_val = 0

#Window function test - works

window.title("Searches")
window.configure(bg='white')
# window.geometry("400x250")

# You have to choose between .grid() and .pack() method, so i will go with .grid()

# Enter words for searching
words_label = tk.Label(window, text='Enter words you want to search here', font=('Helvatica', 13))
words_label.grid(row = 0, columnspan=6)
words = tk.Entry(window, width=100)
words.grid(row = 1, columnspan=6, pady=20)

# Enter words before search
before_label = tk.Label(window, text='Enter words before the searched words',font=('Helvatica', 10))
before_label.grid(row = 2, column = 0, columnspan=3)
before = tk.Entry(window, width=50)
before.grid(row = 3, column = 0, columnspan=3, pady=10)

# Enter words after search
after_label = tk.Label(window, text='Enter words after the searched words',font=('Helvatica', 10))
after_label.grid(row = 2, column = 3, columnspan=3)
after = tk.Entry(window, width=50)
after.grid(row = 3, column = 3, columnspan=3)

# Function for button
def executeClick():
    list_of_words = words.get().split()
    combineWords(list_of_words)
    for word in list_of_words:
         # Google
        if(check_val[0].get()):
            webbrowser.open(f"https://google.com/search?q={before.get()}+{word}+{after.get()}")
        # DuckDuckGo
        if(check_val[1].get()):
            webbrowser.open(f"https://duckduckgo.com/?q={before.get()}+{word}+{after.get()}")
        # Bing
        if(check_val[2].get()):
            webbrowser.open(f"https://bing.com/search?q={before.get()}+{word}+{after.get()}")

# Button
button = tk.Button(window, text="Start searching", command=executeClick)
button.grid(row = 4, column=0, columnspan=1)

# Progress bar
progressBar = ttk.Progressbar(
    window,
    orient = 'horizontal',
    mode='indeterminate',
    length = 400,
    variable=progressBar_val
)
progressBar.grid(row = 4, column=1, columnspan = 5)

# Additional label

label_additional = tk.Label(window, text="Additional settings", font=('Helvatica', 11))
label_additional.grid(row = 5, column = 0, columnspan=6, pady=5)

# Checkboxes
label_checkbox_google     = tk.Label(window, text="Google")
label_checkbox_duckduckgo = tk.Label(window, text="DuckDuckGo")
label_checkbox_bing       = tk.Label(window, text="Bing")
label_checkbox_google.grid    (row = 6, column = 0, columnspan=2)
label_checkbox_duckduckgo.grid(row = 6, column = 2, columnspan=2)
label_checkbox_bing.grid      (row = 6, column = 4, columnspan=2)

checkbox_google     = tk.Checkbutton(window, variable=check_val[0])
checkbox_google.select()
checkbox_duckduckgo = tk.Checkbutton(window, variable=check_val[1])
checkbox_bing       = tk.Checkbutton(window, variable=check_val[2])
checkbox_google.grid    (row = 7, column = 0, columnspan=2)
checkbox_duckduckgo.grid(row = 7, column = 2, columnspan=2)
checkbox_bing.grid      (row = 7, column = 4, columnspan=2)

# Combine words
def combineWords(words):
    for word in words:
        if '+' in word:
            word = word.replace('+', ' ')

# Progress value
def progressBarValue():
    print('TODO')

window.mainloop()