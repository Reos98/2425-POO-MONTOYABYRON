import tkinter as tk
from tkinter import ttk, messagebox

def agregar_tarea():
    """
    Añade una nueva tarea a la lista de tareas.
    """
    tarea = entrada_tarea.get()
    if tarea:  # Verifica que la tarea no esté vacía
        lista_tareas.insert("", tk.END, text=tarea)
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

def marcar_completada():
    """
    Marca una tarea como completada.
    """
    seleccion = lista_tareas.selection()
    if seleccion:
        tarea_id = seleccion[0]
        tarea_texto = lista_tareas.item(tarea_id, "text")
        lista_tareas.item(seleccion[0], text=tarea_texto + " (Completada)")
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

def eliminar_tarea():
    """
    Elimina una tarea de la lista de tareas.
    """
    seleccion = lista_tareas.selection()
    if seleccion:
        lista_tareas.delete(seleccion[0])
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

def manejar_enter(event):
    """
    Manejador de eventos para la tecla Enter.
    Añade la tarea ingresada al presionar Enter.
    """
    agregar_tarea()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x300")  # Establece un tamaño inicial para la ventana

# Crear los widgets
entrada_tarea = tk.Entry(ventana, width=30)
boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
lista_tareas = ttk.Treeview(ventana)  # Usa Treeview para una lista más estilizada
lista_tareas["columns"] = ("tarea",)  # Define las columnas del Treeview
lista_tareas.heading("#0", text="Tarea")  # Encabezado de la columna principal

# Establecer el estilo del Treeview (opcional, para mejorar la apariencia)
estilo = ttk.Style(ventana)
estilo.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white",
                bordercolor="black")
estilo.map("Treeview",
          background=[("selected", "lightblue")],  # Color de fondo al seleccionar
          foreground=[("selected", "black")])  # Color de texto al seleccionar

# Vincular la tecla Enter al campo de entrada
entrada_tarea.bind("<Return>", manejar_enter)

# Colocar los widgets en la ventana
entrada_tarea.pack(pady=10)
boton_agregar.pack(pady=5)
boton_completar.pack(pady=5)
boton_eliminar.pack(pady=5)
lista_tareas.pack(pady=10, fill=tk.BOTH, expand=True)  # La lista se expande con la ventana

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
