"""
Generador de Contraseñas usando Tkinter.

Este programa genera contraseñas aleatorias con opciones para incluir caracteres especiales y elegir la longitud de la contraseña.
"""

import tkinter as tk
import random
import string
from tkinter import messagebox

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador de Contraseñas")
        
        self.create_widgets()
    
    def create_widgets(self):
        length_label = tk.Label(self, text="Longitud de la contraseña:")
        length_label.pack()
        
        self.length_entry = tk.Entry(self)
        self.length_entry.insert(tk.END, "12")  # Establecer longitud predeterminada a 12
        self.length_entry.pack()
        
        self.special_chars_var = tk.BooleanVar()
        special_chars_checkbox = tk.Checkbutton(self, text="Incluir caracteres especiales", variable=self.special_chars_var)
        special_chars_checkbox.pack()
        
        generate_button = tk.Button(self, text="Generar Contraseña", command=self.generate_password)
        generate_button.pack()
    
    def generate_password(self):
        password_length = self.length_entry.get()
        if not password_length.isdigit():
            messagebox.showerror("Error", "La longitud de la contraseña debe ser un número entero.")
            return
        
        password_length = int(password_length)
        include_special_chars = self.special_chars_var.get()
        
        characters = string.ascii_letters + string.digits
        if include_special_chars:
            characters += string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(password_length))
        messagebox.showinfo("Contraseña generada", f"Contraseña generada: {password}")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
