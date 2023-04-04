import random
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import random


def check_word():
    word_input = entry_string.get().lower()
    if word_input == answer:
        output_string.set('Победа! Ответ: ' + answer)
    else:
        output_string.set('Слово ' + word_input + ' не является ответом!')


# выбор случайного слова
random.seed(a = 0) # 0 выбран для тестирования, без указания a берет системное время
with open('words.txt', 'r', encoding='utf-8') as words:
    wordlist = [word.strip() for word in words.readlines()]
    answer = wordlist[random.randrange(len(wordlist))]
    print(answer)
# window
window = ttk.Window(themename= 'journal') # darkly - темный
window.title('Test')
window.geometry('500x150')

# title
title_label = ttk.Label(master = window, text = 'ХЛОВО', font = 'Georgia 18 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_string = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_string)
button = ttk.Button(master = input_frame, text = 'Попробовать', command = check_word)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Вывод', font = 'Georgia 16', textvariable = output_string)
output_label.pack(pady = 5)

window.mainloop()