#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def change():
    if var.get() == 0:
        label['bg'] = 'red'
    elif var.get() == 1:
        label['bg'] = 'green'
    elif var.get() == 2:
        label['bg'] = 'blue'


if __name__ == '__main__':
    # Создание главного окна
    root = Tk()

    var = IntVar()
    var.set(-1)

    # Кнопки
    red = Radiobutton(indicatoron=0, text="Red",
                      variable=var, value=0,
                      command=change, width=10)
    green = Radiobutton(indicatoron=0, text="Green",
                        variable=var, value=1,
                        command=change, width=10)
    blue = Radiobutton(indicatoron=0, text="Blue",
                       variable=var, value=2,
                       command=change, width=10)

    label = Label(width=20, height=10)

    red.pack()
    green.pack()
    blue.pack()
    label.pack()

    root.mainloop()