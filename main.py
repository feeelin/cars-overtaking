import tkinter as tk
from tkinter import *
from methods import *
import tkinter.messagebox as mb


class App(tk.Tk):
    """Main application class"""

    def __init__(self):
        super().__init__()
        self.title('Car replacing')

        # parameters

        self.second_check = BooleanVar()

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

        self.third_car_len = DoubleVar()
        self.third_car_boost = DoubleVar()
        self.third_car_speed = DoubleVar()
        self.third_car_max_speed = DoubleVar()
        self.third_car_x = DoubleVar()

        self.fourth_car_len = DoubleVar()
        self.fourth_car_boost = DoubleVar()
        self.fourth_car_speed = DoubleVar()
        self.fourth_car_max_speed = DoubleVar()
        self.fourth_car_x = DoubleVar()

        self.between_length = DoubleVar()

        self.between_length_2 = DoubleVar()

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

        self.third_car_label = Label(text='A THIRD CAR')

        self.third_car_len_entry = Entry(textvariable=self.third_car_len)
        self.third_car_boost_entry = Entry(textvariable=self.third_car_boost)
        self.third_car_speed_entry = Entry(textvariable=self.third_car_speed)
        self.third_car_max_speed_entry = Entry(textvariable=self.third_car_max_speed)
        self.third_car_x_entry = Entry(textvariable=self.third_car_x)

        self.x_label_3 = Label(text='Coordinate')
        self.speed_label_3 = Label(text='Speed')
        self.boost_label_3 = Label(text='Boost')
        self.max_speed_label_3 = Label(text='Max speed')
        self.len_label_3 = Label(text='Length')

        self.fourth_car_len_entry = Entry(textvariable=self.fourth_car_len)
        self.fourth_car_boost_entry = Entry(textvariable=self.fourth_car_boost)
        self.fourth_car_speed_entry = Entry(textvariable=self.fourth_car_speed)
        self.fourth_car_max_speed_entry = Entry(textvariable=self.fourth_car_max_speed)
        self.fourth_car_x_entry = Entry(textvariable=self.fourth_car_x)

        self.fourth_car_label = Label(text='A FOURTH CAR', pady=5)

        self.x_label_4 = Label(text='Coordinate')
        self.speed_label_4 = Label(text='Speed')
        self.boost_label_4 = Label(text='Boost')
        self.max_speed_label_4 = Label(text='Max speed')
        self.len_label_4 = Label(text='Length')

        self.between_label_2 = Label(text='Between distance')
        self.between_entry_2 = Entry(textvariable=self.between_length_2)

        self.confirm_button = Button(text='Continue', command=self.start)

        self.second_method_check = Checkbutton(text='Oncoming traffic', command=self.oncoming_traffic, var=self.second_check)
        self.third_method_check = Checkbutton(text='Oncoming overtaking', command=self.oncoming_overtaking)

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

        self.second_method_check.grid(row=7, column=4, pady=5)
        self.third_method_check.grid(row=7, column=5)

    def oncoming_traffic(self):
        self.third_car_label.grid(row=8, column=3, pady=10)

        self.x_label_3.grid(row=9, column=5)
        self.speed_label_3.grid(row=9, column=3)
        self.boost_label_3.grid(row=9, column=2)
        self.max_speed_label_3.grid(row=9, column=4)
        self.len_label_3.grid(row=9, column=1)

        self.third_car_len_entry.grid(row=10, column=1)
        self.third_car_boost_entry.grid(row=10, column=2)
        self.third_car_speed_entry.grid(row=10, column=3)
        self.third_car_max_speed_entry.grid(row=10, column=4)
        self.third_car_x_entry.grid(row=10, column=5)

        self.confirm_button.grid(row=11, column=3, pady=5)

    def oncoming_overtaking(self):
        self.fourth_car_label.grid(row=11, column=3, pady=10)

        self.x_label_4.grid(row=12, column=5)
        self.speed_label_4.grid(row=12, column=3)
        self.boost_label_4.grid(row=12, column=2)
        self.max_speed_label_4.grid(row=12, column=4)
        self.len_label_4.grid(row=12, column=1)

        self.fourth_car_len_entry.grid(row=13, column=1)
        self.fourth_car_boost_entry.grid(row=13, column=2)
        self.fourth_car_speed_entry.grid(row=13, column=3)
        self.fourth_car_max_speed_entry.grid(row=13, column=4)
        self.fourth_car_x_entry.grid(row=13, column=5)

        self.between_label_2.grid(row=14, column=1, pady=10)
        self.between_entry_2.grid(row=14, column=2)

        self.confirm_button.grid(row=15, column=3, pady=5)

    def start(self):
        if self.second_check.get():
            self.second_method()
        else:
            self.first_method()

    def first_method(self):
        if self.first_car_x.get() + self.first_car_len.get() > self.second_car_x.get() + self.second_car_len.get():
            _value = first(self.first_car_speed.get(), self.first_car_boost.get(), self.first_car_len.get(),
                           self.first_car_x.get(), self.second_car_x.get(), self.between_length.get(),
                           self.first_car_max_speed.get(), self.second_car_speed.get())
            if _value:
                _msg = 'Overtaking will happen for {} seconds'
                mb.showinfo('Success', _msg.format(_value))
            else:
                _msg = 'Overtaking will not happen'
                mb.showerror('Error', _msg)
        else:
            mb.showerror('Error', 'Incorrect cars positions')

    def second_method(self):
        if self.first_car_x.get() + self.first_car_len.get() > self.second_car_x.get() + self.second_car_len.get():
            _value = second(self.first_car_speed.get(), self.first_car_boost.get(), self.first_car_len.get(),
                            self.first_car_x.get(), self.second_car_x.get(), self.between_length.get(),
                            self.first_car_max_speed.get(), self.second_car_speed.get(), self.third_car_x.get(),
                            self.third_car_speed.get(), self.third_car_boost.get())
            if _value == 'smash':
                _msg = 'Cars will smash'
                mb.showerror('Error', _msg)
            elif _value:
                _msg = 'Overtaking will happen for {} seconds'
                mb.showinfo('Success', _msg.format(_value))
            else:
                _msg = 'Overtaking will not happen'
                mb.showerror('Error', _msg)
        else:
            mb.showerror('Error', 'Incorrect cars positions')


if __name__ == '__main__':
    root = App()
    root.mainloop()
