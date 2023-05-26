import tkinter as tk
from tkinter import messagebox

# Definir una clase para la lista de tareas
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]['completada'] = True

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]

    def mostrar_tareas(self):
        if not self.tareas:
            messagebox.showinfo("Lista de Tareas", "No hay tareas pendientes.")
        else:
            tarea_text = "Hay tareas pendientes:\n"
            for i, tarea in enumerate(self.tareas):
                if not tarea['completada']:
                    tarea_text += f"{i + 1}. {tarea['nombre']}\n"
            messagebox.showinfo("Lista de Tareas", tarea_text)

# Función para agregar una tarea
def agregar_tarea():
    nombre_tarea = entrada_tarea.get().strip()
    if nombre_tarea:
        tarea = {'nombre': nombre_tarea, 'completada': False}
        lista_tareas.agregar_tarea(tarea)
        messagebox.showinfo("Lista de Tareas", "Tarea agregada.")
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Ingrese un nombre de tarea válido.")

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        indice_tarea = int(entrada_indice.get()) - 1
        if 0 <= indice_tarea < len(lista_tareas.tareas):
            lista_tareas.marcar_completada(indice_tarea)
            messagebox.showinfo("Lista de Tareas", "Tarea marcada como completada.")
        else:
            messagebox.showerror("Error", "Índice de tarea inválido.")
    except ValueError:
        messagebox.showerror("Error", "Índice de tarea inválido. Debe ingresar un número.")
    entrada_indice.delete(0, tk.END)

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        indice_tarea = int(entrada_indice.get()) - 1
        if 0 <= indice_tarea < len(lista_tareas.tareas):
            lista_tareas.eliminar_tarea(indice_tarea)
            messagebox.showinfo("Lista de Tareas", "Tarea eliminada.")
        else:
            messagebox.showerror("Error", "Índice de tarea inválido.")
    except ValueError:
        messagebox.showerror("Error", "Índice de tarea inválido. Debe ingresar un número.")
    entrada_indice.delete(0, tk.END)

# Función para mostrar las tareas pendientes
def mostrar_tareas():
    lista_tareas.mostrar_tareas()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Lista de Tareas")
ventana.configure(bg="turquoise")

# Definir el estilo de fuente
estilo_fuente = ("Arial", 14)

# Crear los elementos de la interfaz
etiqueta_tarea = tk.Label(ventana, text="Ingrese el nombre de la tarea:", font=estilo_fuente, bg="turquoise")
etiqueta_tarea.pack()

entrada_tarea = tk.Entry(ventana, font=estilo_fuente)
entrada_tarea.pack()

boton_agregar = tk.Button(ventana, text="Agregar tarea", font=estilo_fuente, command=agregar_tarea)
boton_agregar.pack()

etiqueta_indice = tk.Label(ventana, text="Ingrese el número de la tarea:", font=estilo_fuente, bg="turquoise")
etiqueta_indice.pack()

entrada_indice = tk.Entry(ventana, font=estilo_fuente)
entrada_indice.pack()

boton_marcar_completada = tk.Button(ventana, text="Marcar como completada", font=estilo_fuente, command=marcar_completada)
boton_marcar_completada.pack()

boton_eliminar = tk.Button(ventana, text="Eliminar tarea", font=estilo_fuente, command=eliminar_tarea)
boton_eliminar.pack()

boton_mostrar = tk.Button(ventana, text="Mostrar tareas pendientes", font=estilo_fuente, command=mostrar_tareas)
boton_mostrar.pack()

boton_salir = tk.Button(ventana, text="Salir", font=estilo_fuente, command=ventana.quit)
boton_salir.pack()

# Crear una instancia de la lista de tareas
lista_tareas = ListaTareas()

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()
