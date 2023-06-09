from flask import Flask, render_template, request

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
            return "Tarea agregada correctamente."
        else:
            return "La descripción de la tarea no puede estar vacía."

    def obtener_tareas(self):
        return self.tareas

    def marcar_completada(self, num_tarea):
        if 1 <= num_tarea <= len(self.tareas):
            tarea = self.tareas[num_tarea - 1]
            tarea.marcar_completada()
            return "Tarea marcada como completada."
        else:
            return "Número de tarea inválido."

    def marcar_pendiente(self, num_tarea):
        if 1 <= num_tarea <= len(self.tareas):
            tarea = self.tareas[num_tarea - 1]
            tarea.marcar_pendiente()
            return "Tarea marcada como pendiente."
        else:
            return "Número de tarea inválido."

    def eliminar_tarea(self, num_tarea):
        if 1 <= num_tarea <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(num_tarea - 1)
            return f"Tarea eliminada: {tarea_eliminada.descripcion}"
        else:
            return "Número de tarea inválido."


app = Flask(__name__)
lista_tareas = ListaTareasApp()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        mensaje = lista_tareas.agregar_tarea(descripcion)
        tareas = lista_tareas.obtener_tareas()
        return render_template('index.html', mensaje=mensaje, tareas=tareas)
    else:
        tareas = lista_tareas.obtener_tareas()
        return render_template('index.html', tareas=tareas)


@app.route('/marcar_completada/<int:num_tarea>')
def marcar_completada(num_tarea):
    mensaje = lista_tareas.marcar_completada(num_tarea)
    tareas = lista_tareas.obtener_tareas()
    return render_template('index.html', mensaje=mensaje, tareas=tareas)


@app.route('/marcar_pendiente/<int:num_tarea>')
def marcar_pendiente(num_tarea):
    mensaje = lista_tareas.marcar_pendiente(num_tarea)
    tareas = lista_tareas.obtener_tareas()
    return render_template('index.html', mensaje=mensaje, tareas=tareas)


@app.route('/eliminar_tarea/<int:num_tarea>')
def eliminar_tarea(num_tarea):
    mensaje = lista_tareas.eliminar_tarea(num_tarea)
    tareas = lista_tareas.obtener_tareas()
    return render_template('index.html', mensaje=mensaje, tareas=tareas)


if __name__ == '__main__':
    app.run()
