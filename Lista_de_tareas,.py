class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def marcar_pendiente(self):
        self.completada = False


class ListaTareasApp:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        if descripcion:
            tarea = Tarea(descripcion)
            self.tareas.append(tarea)
            print("Tarea agregada correctamente.")
        else:
            print("La descripción de la tarea no puede estar vacía.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for i, tarea in enumerate(self.tareas, start=1):
                estado = "Completada" if tarea.completada else "Pendiente"
                print(f"{i}. {tarea.descripcion} - Estado: {estado}")
        else:
            print("No hay tareas.")

    def marcar_completada(self):
        if self.tareas:
            try:
                num_tarea = int(input("Ingrese el número de tarea completada: "))

                if 1 <= num_tarea <= len(self.tareas):
                    tarea = self.tareas[num_tarea - 1]
                    tarea.marcar_completada()
                    print("Tarea marcada como completada.")
                else:
                    print("Número de tarea inválido.")
            except ValueError:
                print("Número de tarea inválido. Debe ingresar un número.")

        else:
            print("No hay tareas.")

    def marcar_pendiente(self):
        if self.tareas:
            try:
                num_tarea = int(input("Ingrese el número de tarea pendiente: "))

                if 1 <= num_tarea <= len(self.tareas):
                    tarea = self.tareas[num_tarea - 1]
                    tarea.marcar_pendiente()
                    print("Tarea marcada como pendiente.")
                else:
                    print("Número de tarea inválido.")
            except ValueError:
                print("Número de tarea inválido. Debe ingresar un número.")
        else:
            print("No hay tareas.")

    def eliminar_tarea(self):
        if self.tareas:
            try:
                num_tarea = int(input("Ingrese el número de tarea a eliminar: "))

                if 1 <= num_tarea <= len(self.tareas):
                    tarea_eliminada = self.tareas.pop(num_tarea - 1)
                    print(f"Tarea eliminada: {tarea_eliminada.descripcion}")
                else:
                    print("Número de tarea inválido.")
            except ValueError:
                print("Número de tarea inválido. Debe ingresar un número.")
        else:
            print("No hay tareas.")

    def ejecutar(self):
        while True:
            print("\n--- Lista de Tareas ---")
            print("1. Agregar tarea")
            print("2. Mostrar tareas")
            print("3. Marcar tarea como completada")
            print("4. Marcar tarea como pendiente")
            print("5. Eliminar tarea")
            print("6. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                descripcion = input("Ingrese la descripción de la tarea: ")
                self.agregar_tarea(descripcion)
            elif opcion == "2":
                self.mostrar_tareas()
            elif opcion == "3":
                self.marcar_completada()
            elif opcion == "4":
                self.marcar_pendiente()
            elif opcion == "5":
                self.eliminar_tarea()
            elif opcion == "6":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")


# Crear la instancia de la aplicación y ejecutarla
app = ListaTareasApp()
app.ejecutar()
