import tkinter
import customtkinter as tk
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
app = tk.CTk()
app.geometry("240x400")

def button1():
    text = entry.get()
    print(text)

button = tk.CTkButton(master = app, text="Prueba", command = button1)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

entry = tk.CTkEntry(master=app,
                    width=120,
                    height=25,
                    corner_radius=10)
entry.place(relx=0.50, rely=0.75, anchor=tkinter.CENTER)

app.mainloop()