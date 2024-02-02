#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox


def open_file():
    try:
        text.delete(1.0, tk.END)
        file = entry.get()
        with open(file, 'r', encoding="utf-8") as f:
            data = f.read()
        text.insert(1.0, data)
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл не найден")


def save_file():
    try:
        file = entry.get()
        data = text.get(1.0, tk.END)
        with open(file, 'w', encoding="utf-8") as f:
            f.write(data)
        messagebox.showinfo("Сохранено", "Файл успешно сохранен")
    except:
        messagebox.showerror("Ошибка", "Не удалось сохранить файл")


if __name__ == '__main__':
    # Создание главного окна
    root = tk.Tk()

    entry = tk.Entry(width=20)
    text = tk.Text(width=50, height=30)

    # Кнопки
    but_open = tk.Button(text='Открыть', width=10, pady=5, command=open_file)
    but_save = tk.Button(text='Сохранить', width=10, pady=5, command=save_file)

    entry.pack(padx=3, pady=5)
    but_open.pack(padx=3, pady=5)
    but_save.pack(padx=3, pady=5)
    text.pack(padx=3, pady=10)

    root.mainloop()