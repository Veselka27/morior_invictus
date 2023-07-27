import customtkinter as tk
from CTkMessagebox import CTkMessagebox as messagebox

morse = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    " " : ""
    }

def convert():
    text = entry.get().lower()
    if text != "":
        try:
            translated_text = "|||"

            for letter in text:
                translated_text += morse[letter]
                translated_text += "|"

            translated_text += "||"

            #messagebox(master=root, title="Morse", icon="info", message=f"Translated text:\n{translated_text}")
            morse_output.set(translated_text)
        except KeyError:
            messagebox(master=root, title="Error", icon="cancel", message="You can't convert special characters!")

def enter(event):
   if event.keysym == "Return":
    convert()

def close():
    msg = messagebox(master=root, title="Exit?", message="Do you want to close the program?", icon="question", option_1="Yes", option_2="Cancel")
    response = msg.get()
    if response=="Yes":
        root.destroy()      

def clear():
    entry.delete(0, tk.END)
    morse_output.set("")

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
root = tk.CTk()
root.title("Morse converter")
root.geometry("350x200")
label = tk.CTkLabel(root, text="Morse converter", font=('arial', 17))
label.pack(padx=20, pady=20)
entry = tk.CTkEntry(root)
entry.bind("<KeyPress>", enter)
entry.pack()
morse_output = tk.StringVar()
output = tk.CTkLabel(root, font=('arial', 15), textvariable=morse_output)
output.pack()
button = tk.CTkButton(root, text="Convert", font=('arial', 13), command=convert)
button.pack(pady=10)
clsbutton = tk.CTkButton(root, text="Clear", font=("arial", 13), command=clear)
clsbutton.pack()
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
