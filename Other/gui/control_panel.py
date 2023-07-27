from customtkinter import *
from time import sleep
import threading
set_appearance_mode("dark")
set_default_color_theme("dark-blue")

root = CTk()
root.title("Control Panel")
root.geometry("500x400")
label = CTkLabel(root, text="Control Panel", font=('arial', 20)).pack(padx=20, pady=20)
led1 = CTkSwitch(root, text="Red").pack()
led2 = CTkSwitch(root, text="Green").pack()
led3 = CTkSwitch(root, text="Yellow").pack()
frequency_label = CTkLabel(root, text="Frequency", font=('arial', 17)).pack(pady=5)
frequency_slider = CTkSlider(root).pack(pady=10)
brightess_label = CTkLabel(root, text="Brightness", font=('arial', 17)).pack(pady=5)
brightess_slider = CTkSlider(root).pack(pady=10)
root.mainloop()