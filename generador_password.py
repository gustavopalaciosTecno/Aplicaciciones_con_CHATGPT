import tkinter as tk
import random
import string
from tkinter import messagebox
import tkinter.ttk as ttk
import pyperclip

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador de Contraseñas")
        self.configure(bg="#009688")  # Color de fondo verde turquesa
        
        self.special_chars_var = tk.BooleanVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        length_label = tk.Label(self, text="Longitud de la contraseña:", bg="#009688", fg="white")  # Color de fondo y texto blanco
        length_label.pack()
        
        self.length_entry = tk.Entry(self)
        self.length_entry.insert(tk.END, "12")  # Establecer longitud predeterminada a 12
        self.length_entry.pack()
        
        special_chars_checkbox = tk.Checkbutton(self, text="Incluir caracteres especiales", variable=self.special_chars_var, bg="#009688", fg="white")  # Color de fondo y texto blanco
        special_chars_checkbox.pack()
        
        generate_button = tk.Button(self, text="Generar Contraseña", command=self.generate_password, bg="#4CAF50", fg="white")  # Color de fondo verde y texto blanco
        generate_button.pack()
        
        self.password_label = tk.Label(self, text="Contraseña generada:", bg="#009688", fg="white")  # Color de fondo y texto blanco
        self.password_label.pack()
        
        self.password_entry = ttk.Entry(self, state="readonly")
        self.password_entry.pack()
        
        copy_button = tk.Button(self, text="Copiar Contraseña", command=self.copy_password, bg="#4CAF50", fg="white")  # Color de fondo verde y texto blanco
        copy_button.pack()
    
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
        self.password_entry.configure(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)
        self.password_entry.configure(state="readonly")
    
    def copy_password(self):
        password = self.password_entry.get()
        self.clipboard_clear()
        self.clipboard_append(password)
        self.update()
        messagebox.showinfo("Contraseña Copiada", "La contraseña ha sido copiada al portapapeles.")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
