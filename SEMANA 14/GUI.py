import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame para la entrada de datos
        self.frame_inputs = tk.Frame(root)
        self.frame_inputs.pack(pady=10)

        tk.Label(self.frame_inputs, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_inputs, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_inputs, width=15)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_inputs, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.add_button = tk.Button(self.frame_buttons, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.frame_buttons, text="Eliminar Evento", command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.exit_button = tk.Button(self.frame_buttons, text="Salir", command=root.quit)
        self.exit_button.grid(row=0, column=2, padx=5)

        # Tabla de eventos
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=20)

    def add_event(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos deben estar completos")

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Seleccione un evento para eliminar")
            return

        confirm = messagebox.askyesno("Confirmación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()