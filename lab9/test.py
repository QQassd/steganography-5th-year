import tkinter as tk
from tkinter import Tk, Label, Button, scrolledtext, filedialog, StringVar
from tkinter.ttk import Radiobutton
from PIL import Image, ImageTk
import random
import numpy as np
from os import path

class StegoRGBApp:
    def __init__(self, window):
        self.window = window
        self.window.minsize(width=1040, height=1)
        self.window.title('StegoRGB')

        self.file = None
        self.image_for_ext = None
        self.lenmes = 0

        self.create_widgets()

    def create_widgets(self):
        Label(self.window, text='Сообщение', font=('Times New Roman', 14)).grid(column=0, row=0, pady=10, padx=10, sticky='W')
        self.scr = scrolledtext.ScrolledText(self.window, width=60, height=8)
        self.scr.grid(column=0, row=1, padx=10)
        self.scr.focus()

        Label(self.window, text='Контейнер', font=('Times New Roman', 14)).grid(column=1, row=0, pady=10, padx=10, sticky='W')
        Button(self.window, text="Выберите изображение", command=self.clicked).grid(column=1, row=1, padx=10, pady=10, sticky='N')

        self.lbl11 = Label(self.window, text='', font=('Times New Roman', 9))
        self.lbl11.place(x=530, y=90)

        Label(self.window, text='Метод скрытия', font=('Times New Roman', 14)).grid(column=2, row=0, pady=10, padx=10, sticky='W')
        self.var1 = StringVar()
        self.rad1 = Radiobutton(self.window, text='LSB-R', value=1, variable=self.var1, command=self.enable_raid)
        self.rad2 = Radiobutton(self.window, text='LSB-M', value=2, variable=self.var1, command=self.enable_raid)
        self.rad3 = Radiobutton(self.window, text='Код Хемминга', value=3, variable=self.var1, command=self.disable_raid)
        self.rad1.place(x=725, y=55)
        self.rad2.place(x=725, y=75)
        self.rad3.place(x=725, y=95)

        Label(self.window, text='Рейт', font=('Times New Roman', 14)).grid(column=3, row=0, pady=10, padx=30, sticky='W')
        self.var2 = StringVar()
        self.rad2_1 = Radiobutton(self.window, text='1', value=1, variable=self.var2, state='disabled')
        self.rad2_2 = Radiobutton(self.window, text='2', value=2, variable=self.var2, state='disabled')
        self.rad2_3 = Radiobutton(self.window, text='3', value=3, variable=self.var2, state='disabled')
        self.rad2_4 = Radiobutton(self.window, text='4', value=4, variable=self.var2, state='disabled')
        self.rad2_5 = Radiobutton(self.window, text='5', value=5, variable=self.var2, state='disabled')
        self.rad2_6 = Radiobutton(self.window, text='6', value=6, variable=self.var2, state='disabled')
        self.rad2_7 = Radiobutton(self.window, text='7', value=7, variable=self.var2, state='disabled')
        self.rad2_8 = Radiobutton(self.window, text='8', value=8, variable=self.var2, state='disabled')
        self.rad2_1.place(x=850, y=55)
        self.rad2_2.place(x=850, y=75)
        self.rad2_3.place(x=850, y=95)
        self.rad2_4.place(x=850, y=115)
        self.rad2_5.place(x=890, y=55)
        self.rad2_6.place(x=890, y=75)
        self.rad2_7.place(x=890, y=95)
        self.rad2_8.place(x=890, y=115)

        Button(self.window, text="Произвести скрытие", width=25, command=self.hiding).grid(column=0, row=3, padx=0, pady=10, columnspan=2)
        Button(self.window, text="Извлечь сообщение", width=25, command=self.extraction).grid(column=1, row=3, padx=0, pady=10, columnspan=2)

    def clicked(self):
        self.file = filedialog.askopenfilename(filetypes=(("Image files", "*.bmp"), ("all files", "*.*")), initialdir=path.dirname(__file__))
        if self.file:
            self.lbl11.configure(text=path.basename(self.file))

    def enable_raid(self):
        for i in range(1, 9):
            getattr(self, f'rad2_{i}').configure(state='enabled')

    def disable_raid(self):
        for i in range(1, 9):
            getattr(self, f'rad2_{i}').configure(state='disabled')

    def hiding(self):
        if self.var1.get() == '1':
            # Implement LSB-R hiding method
            pass
        elif self.var1.get() == '2':
            # Implement LSB-M hiding method
            pass
        elif self.var1.get() == '3':
            # Implement Hamming code hiding method
            pass

    def extraction(self):
        if self.var1.get() in ('1', '2'):
            # Extract message using LSB-R or LSB-M method
            pass
        elif self.var1.get() == '3':
            # Extract message using Hamming code method
            pass

if __name__ == "__main__":
    window = Tk()
    StegoRGBApp(window)
    window.mainloop()
