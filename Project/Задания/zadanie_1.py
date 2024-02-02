#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk


def sum():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x + y

        result['text']=str(res)
    except:
        result['text']="Ошибка"


def sub():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x - y

        result['text'] = str(res)
    except:
        result['text'] = "Ошибка"


def div():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x / y

        result['text'] = str(res)
    except:
        result['text'] = "Ошибка"


def mult():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x * y

        result['text'] = str(res)
    except:
        result['text'] = "Ошибка"


if __name__ == '__main__':
    # Создание главного окна
    root = tk.Tk()

    # Текстовые поля для ввода чисел
    entry_1 = tk.Entry(root)
    entry_2 = tk.Entry(root)
    result = tk.Label()

    # Кнопки операций
    but_sum = tk.Button(text="+", command=sum)
    but_sub = tk.Button(text="-", command=sub)
    but_mult = tk.Button(text="*", command=mult)
    but_div = tk.Button(text="/", command=div)

    entry_1.pack()
    entry_2.pack()
    but_sum.pack()
    but_sub.pack()
    but_mult.pack()
    but_div.pack()
    result.pack()

    root.mainloop()