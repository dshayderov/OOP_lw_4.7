#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk


def red():
    entry.delete(0, tk.END)
    entry.insert(0, "#ff0000")
    res['text'] = 'Красный'


def orange():
    entry.delete(0, tk.END)
    entry.insert(0, "#ff7d00")
    res['text'] = 'Оранжевый'


def yellow():
    entry.delete(0, tk.END)
    entry.insert(0, "#ffff00")
    res['text'] = 'Жёлтый'


def green():
    entry.delete(0, tk.END)
    entry.insert(0, "#00ff00")
    res['text'] = 'Зелёный'


def blue():
    entry.delete(0, tk.END)
    entry.insert(0, "#007dff")
    res['text'] = 'Голубой'


def indigo():
    entry.delete(0, tk.END)
    entry.insert(0, "#0000ff")
    res['text'] = 'Синий'


def violet():
    entry.delete(0, tk.END)
    entry.insert(0, "#7d00ff")
    res['text'] = 'Фиолетовый'


if __name__ == '__main__':
    # Создание главного окна
    root = tk.Tk()

    res = tk.Label()
    entry = tk.Entry(width=30)

    # Кнопки цветов
    but_red = tk.Button(bg='#ff0000', width=30, pady=5, command=red)
    but_orange = tk.Button(bg='#ff7d00', width=30, pady=5, command=orange)
    but_yellow = tk.Button(bg='#ffff00', width=30, pady=5, command=yellow)
    but_green = tk.Button(bg='#00ff00', width=30, pady=5, command=green)
    but_blue = tk.Button(bg='#007dff', width=30, pady=5, command=blue)
    but_indigo = tk.Button(bg='#0000ff', width=30, pady=5, command=indigo)
    but_violet = tk.Button(bg='#7d00ff', width=30, pady=5, command=violet)

    res.pack()
    entry.pack()
    but_red.pack()
    but_orange.pack()
    but_yellow.pack()
    but_green.pack()
    but_blue.pack()
    but_indigo.pack()
    but_violet.pack()

    root.mainloop()
