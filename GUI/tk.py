import tkinter as tk
from tkinter import messagebox

def greet():
    nome = entry.get()
    if nome:
        messagebox.showinfo("Comprimentando", f"Olá, {nome}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create the main window
root = tk.Tk()
root.title("Aplicativo Inicial")
root.geometry("300x150")

# Create and place widgets
label = tk.Label(root, text="Escreva seu nome:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Dizer olá", command=greet)
button.pack(pady=10)

# Run the application
root.mainloop()
