import tkinter as tk
from tkinter import *
from methods import *


class App(tk.Tk):
    """Main application class"""

    def __init__(self):
        super().__init__()
        self.title('Car replacing')

        # parameters

        self.first_car_len = DoubleVar()
        self.first_car_boost = DoubleVar()
        self.first_car_speed = DoubleVar()
        self.first_car_max_speed = DoubleVar()
        self.first_car_x = DoubleVar()

        self.second_car_len = DoubleVar()
        self.second_car_boost = DoubleVar()
        self.second_car_speed = DoubleVar()
        self.second_car_max_speed = DoubleVar()
        self.second_car_x = DoubleVar()

        self.between_length = DoubleVar()

        # interface
        self.first_car_label = Label(text='A FIRST CAR', pady=5)

        self.first_car_len_entry = Entry(textvariable=self.first_car_len)
        self.first_car_boost_entry = Entry(textvariable=self.first_car_boost)
        self.first_car_speed_entry = Entry(textvariable=self.first_car_speed)
        self.first_car_max_speed_entry = Entry(textvariable=self.first_car_max_speed)
        self.first_car_x_entry = Entry(textvariable=self.first_car_x)

        self.second_car_label = Label(text='A SECOND CAR', pady=5)

        self.second_car_len_entry = Entry(textvariable=self.second_car_len)
        self.second_car_boost_entry = Entry(textvariable=self.second_car_boost)
        self.second_car_speed_entry = Entry(textvariable=self.second_car_speed)
        self.second_car_max_speed_entry = Entry(textvariable=self.second_car_max_speed)
        self.second_car_x_entry = Entry(textvariable=self.second_car_x)

        self.x_label_1 = Label(text='Coordinate')
        self.speed_label_1 = Label(text='Speed')
        self.boost_label_1 = Label(text='Boost')
        self.max_speed_label_1 = Label(text='Max speed')
        self.len_label_1 = Label(text='Length')

        self.x_label_2 = Label(text='Coordinate')
        self.speed_label_2 = Label(text='Speed')
        self.boost_label_2 = Label(text='Boost')
        self.max_speed_label_2 = Label(text='Max speed')
        self.len_label_2 = Label(text='Length')

        self.between_label = Label(text='Between distance')
        self.between_entry = Entry(textvariable=self.between_length)

        self.confirm_button = Button(text='Confirm', command=self.start)

        # packing

        self.first_car_label.grid(row=1, column=3)

        self.x_label_1.grid(row=2, column=5)
        self.speed_label_1.grid(row=2, column=3)
        self.boost_label_1.grid(row=2, column=2)
        self.max_speed_label_1.grid(row=2, column=4)
        self.len_label_1.grid(row=2, column=1)

        self.first_car_len_entry.grid(row=3, column=1)
        self.first_car_boost_entry.grid(row=3, column=2)
        self.first_car_speed_entry.grid(row=3, column=3)
        self.first_car_max_speed_entry.grid(row=3, column=4)
        self.first_car_x_entry.grid(row=3, column=5)

        self.second_car_label.grid(row=4, column=3)

        self.x_label_2.grid(row=5, column=5)
        self.speed_label_2.grid(row=5, column=3)
        self.boost_label_2.grid(row=5, column=2)
        self.max_speed_label_2.grid(row=5, column=4)
        self.len_label_2.grid(row=5, column=1)

        self.second_car_len_entry.grid(row=6, column=1)
        self.second_car_boost_entry.grid(row=6, column=2)
        self.second_car_speed_entry.grid(row=6, column=3)
        self.second_car_max_speed_entry.grid(row=6, column=4)
        self.second_car_x_entry.grid(row=6, column=5, pady=5)

        self.between_label.grid(row=7, column=1, pady=5)
        self.between_entry.grid(row=7, column=2)

        self.confirm_button.grid(row=8, column=3, pady=5)

    def start(self):
        if self.first_car_x.get() + self.first_car_len.get() > self.second_car_x.get() + self.second_car_len.get():
            print(classicTask(self.first_car_speed.get(), self.first_car_boost.get(), self.first_car_len.get(),
                              self.first_car_x.get(), self.second_car_speed.get(), self.second_car_boost.get(),
                              self.second_car_len.get(), self.second_car_x.get()))


if __name__ == '__main__':
    root = App()
    root.mainloop()
