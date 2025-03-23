import tkinter as tk
from tkinter import ttk, messagebox


# Función para agregar un texto a la lista
def guardar_texto():
    texto = entrada_texto.get()
    if texto:
        tabla.insert("", "end", values=(texto,))
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")


# Función para eliminar un texto seleccionado
def eliminar_texto():
    seleccionado = tabla.selection()
    if seleccionado:
        tabla.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un elemento para eliminar.")


# Función para eliminar todos los textos
def eliminar_todos():
    for item in tabla.get_children():
        tabla.delete(item)


# Función para modificar un texto seleccionado
def modificar_texto():
    seleccionado = tabla.selection()
    if seleccionado:
        nuevo_texto = entrada_texto.get()
        if nuevo_texto:
            tabla.item(seleccionado, values=(nuevo_texto,))  # Modifica el texto seleccionado
            entrada_texto.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo de texto está vacío.")
    else:
        messagebox.showwarning("Advertencia", "Selecciona un elemento para modificar.")


# Función para seleccionar un elemento y colocarlo en el campo de texto
def seleccionar_texto(event):
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado, "values")
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(0, valores[0])


# Función para salir de la aplicación
def salir():
    ventana.quit()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Textos")
ventana.geometry("500x400")
ventana.configure(bg="#D6EAF8")

# Etiqueta y campo de texto
tk.Label(ventana, text="Texto:", bg="#D6EAF8", font=("Arial", 12)).pack(pady=5)
entrada_texto = tk.Entry(ventana, font=("Arial", 12))
entrada_texto.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana, bg="#D6EAF8")
frame_botones.pack(pady=5)

tk.Button(frame_botones, text="Guardar", command=guardar_texto, width=10).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="Modificar", command=modificar_texto, width=10).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="Eliminar", command=eliminar_texto, width=10).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_botones, text="Eliminar Todos", command=eliminar_todos, width=12).grid(row=0, column=3, padx=5, pady=5)
tk.Button(frame_botones, text="Salir", command=salir, width=10, bg="red", fg="white").grid(row=0, column=4, padx=5,
                                                                                           pady=5)

# Tabla para mostrar los textos guardados
tabla = ttk.Treeview(ventana, columns=("Texto"), show="headings", height=10)
tabla.heading("Texto", text="Texto")
tabla.pack(pady=10)

# Evento para seleccionar un texto y colocarlo en la entrada
tabla.bind("<ButtonRelease-1>", seleccionar_texto)

# Ejecutar el bucle de eventos
ventana.mainloop()