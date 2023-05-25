import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def convertir():
    try:
        km = float(entrada_km.get())
        millas = km * 0.621371
        messagebox.showinfo("Resultado", f"{km} kilómetros son {millas} millas.")
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa un número válido!")

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.title("Conversor de kilómetros a millas")
ventana.geometry("400x400")
ventana.resizable(False, False)

style = ttk.Style()
style.configure("TFrame", background="black")
style.configure("TLabel", background="black", foreground="white", font=("Arial", 14))
style.configure("TEntry", font=("Arial", 14))
style.configure("TButton", font=("Arial", 14, "bold"), relief="solid", borderwidth=0)

style.map("TButton",
          background=[("active", "green"), ("disabled", "gray")],
          foreground=[("active", "green"), ("disabled", "gray")])

frame_principal = ttk.Frame(ventana, style="TFrame")
frame_principal.pack(expand=True, padx=20, pady=20)

etiqueta_km = ttk.Label(frame_principal, text="Kilómetros:")
etiqueta_km.pack(pady=10)

entrada_km = ttk.Entry(frame_principal, style="TEntry")
entrada_km.pack()

boton_convertir = ttk.Button(frame_principal, text="Convertir", command=convertir, style="TButton")
boton_convertir.pack(pady=10)

boton_salir = ttk.Button(frame_principal, text="Salir", command=salir, style="TButton")
boton_salir.pack(pady=10)

ventana.mainloop()
