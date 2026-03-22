import tkinter as tk
from tkinter import ttk, messagebox


class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("700x480")
        self.root.resizable(False, False)

        self._construir_formulario()
        self._construir_botones()
        self._construir_tabla()

    # ── Formulario ──────────────────────────────────────────
    def _construir_formulario(self):
        frame = tk.LabelFrame(self.root, text="Datos del Visitante", padx=10, pady=10)
        frame.pack(fill="x", padx=15, pady=10)

        # Cédula
        tk.Label(frame, text="Cédula:").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_cedula = tk.Entry(frame, width=30)
        self.entry_cedula.grid(row=0, column=1, padx=10, pady=4)

        # Nombre
        tk.Label(frame, text="Nombre completo:").grid(row=1, column=0, sticky="w", pady=4)
        self.entry_nombre = tk.Entry(frame, width=30)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=4)

        # Motivo
        tk.Label(frame, text="Motivo de visita:").grid(row=2, column=0, sticky="w", pady=4)
        self.entry_motivo = tk.Entry(frame, width=30)
        self.entry_motivo.grid(row=2, column=1, padx=10, pady=4)

    # ── Botones ─────────────────────────────────────────────
    def _construir_botones(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        tk.Button(frame, text="Registrar", width=15, bg="#4CAF50", fg="white",
                  command=self._registrar).grid(row=0, column=0, padx=8)

        tk.Button(frame, text="Eliminar", width=15, bg="#f44336", fg="white",
                  command=self._eliminar).grid(row=0, column=1, padx=8)

        tk.Button(frame, text="Limpiar Campos", width=15,
                  command=self._limpiar).grid(row=0, column=2, padx=8)

    # ── Tabla ────────────────────────────────────────────────
    def _construir_tabla(self):
        frame = tk.LabelFrame(self.root, text="Lista de Visitantes", padx=10, pady=10)
        frame.pack(fill="both", expand=True, padx=15, pady=10)

        columnas = ("cedula", "nombre", "motivo")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10)

        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre Completo")
        self.tabla.heading("motivo", text="Motivo de Visita")

        self.tabla.column("cedula", width=120, anchor="center")
        self.tabla.column("nombre", width=220)
        self.tabla.column("motivo", width=270)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ── Acciones ─────────────────────────────────────────────
    def _registrar(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        exito = self.servicio.registrar(cedula, nombre, motivo)
        if exito:
            messagebox.showinfo("Éxito", f"Visitante '{nombre}' registrado correctamente.")
            self._actualizar_tabla()
            self._limpiar()
        else:
            messagebox.showerror("Error", f"La cédula '{cedula}' ya está registrada.")

    def _eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Seleccione un visitante de la lista.")
            return

        item = self.tabla.item(seleccion[0])
        cedula = item["values"][0]
        nombre = item["values"][1]

        confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar a '{nombre}'?")
        if confirmar:
            self.servicio.eliminar(cedula)
            self._actualizar_tabla()

    def _limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)
        self.entry_cedula.focus()

    def _actualizar_tabla(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for v in self.servicio.obtener_todos():
            self.tabla.insert("", "end", values=(v.cedula, v.nombre, v.motivo))