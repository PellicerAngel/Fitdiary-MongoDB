import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Entrenamiento")
        self.root.geometry("400x500")
        self.conexion_bd = sqlite3.connect("entrenamiento.db")
        self.crear_tablas()
        self.usuario_actual = None
        self.mostrar_inicio_sesion()

    def crear_tablas(self):
        cursor = self.conexion_bd.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usuario TEXT UNIQUE NOT NULL,
                            contraseña TEXT NOT NULL,
                            edad INTEGER,
                            dni TEXT UNIQUE,
                            altura REAL,
                            genero TEXT,
                            peso REAL,
                            grasa_corporal REAL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usuario TEXT NOT NULL,
                            fecha TEXT NOT NULL,
                            duracion INTEGER NOT NULL,
                            tipo_entrenamiento TEXT NOT NULL,
                            FOREIGN KEY (usuario) REFERENCES usuarios(usuario))''')
        self.conexion_bd.commit()

    def mostrar_inicio_sesion(self):
        self.limpiar_ventana()
        self.inicio_sesion_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.inicio_sesion_frame.pack(padx=20, pady=20)

        tk.Label(self.inicio_sesion_frame, text="Usuario:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.inicio_sesion_frame, text="Contraseña:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.usuario_entry = tk.Entry(self.inicio_sesion_frame, bg="white", font=("Helvetica", 12))
        self.usuario_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self.inicio_sesion_frame, show="*", bg="white", font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.iniciar_sesion_button = tk.Button(self.inicio_sesion_frame, text="Iniciar Sesión", command=self.iniciar_sesion, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.iniciar_sesion_button.grid(row=2, columnspan=2, pady=10)
        self.registrarse_button = tk.Button(self.inicio_sesion_frame, text="Registrarse", command=self.mostrar_registro, bg="#2196F3", fg="white", font=("Helvetica", 12))
        self.registrarse_button.grid(row=3, columnspan=2, pady=10)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()

        cursor = self.conexion_bd.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (usuario, password))
        usuario_data = cursor.fetchone()

        if usuario_data:
            self.usuario_actual = usuario
            self.mostrar_menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def mostrar_registro(self):
        self.limpiar_ventana()
        self.registro_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.registro_frame.pack(padx=20, pady=20)

        # Labels
        tk.Label(self.registro_frame, text="Usuario:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Contraseña:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Edad:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="DNI:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Altura (cm):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Género:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Peso (kg):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Grasa Corporal (%):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)

        # Entries
        self.usuario_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.usuario_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self.registro_frame, show="*", bg="white", font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.edad_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.edad_entry.grid(row=2, column=1, padx=5, pady=5)
        self.dni_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.dni_entry.grid(row=3, column=1, padx=5, pady=5)
        self.altura_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.altura_entry.grid(row=4, column=1, padx=5, pady=5)
        self.genero_combobox = ttk.Combobox(self.registro_frame, values=["Masculino", "Femenino"], state="readonly")
        self.genero_combobox.grid(row=5, column=1, padx=5, pady=5)
        self.peso_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.peso_entry.grid(row=6, column=1, padx=5, pady=5)
        self.grasa_corporal_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.grasa_corporal_entry.grid(row=7, column=1, padx=5, pady=5)

        # Buttons
        self.registrar_button = tk.Button(self.registro_frame, text="Registrar", command=self.registrar_usuario, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.registrar_button.grid(row=8, columnspan=2, pady=10)
        self.cancelar_button = tk.Button(self.registro_frame, text="Cancelar", command=self.mostrar_inicio_sesion, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancelar_button.grid(row=9, columnspan=2, pady=10)

    def registrar_usuario(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()
        edad = self.edad_entry.get()
        dni = self.dni_entry.get()
        altura = self.altura_entry.get()
        genero = self.genero_combobox.get()
        peso = self.peso_entry.get()
        grasa_corporal = self.grasa_corporal_entry.get()

        if not (usuario and password and edad and dni and altura and genero and peso and grasa_corporal):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            cursor = self.conexion_bd.cursor()
            cursor.execute('''INSERT INTO usuarios (usuario, contraseña, edad, dni, altura, genero, peso, grasa_corporal)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (usuario, password, edad, dni, altura, genero, peso, grasa_corporal))
            self.conexion_bd.commit()
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
            self.mostrar_inicio_sesion()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El usuario o DNI ya existe.")

    def mostrar_menu(self):
        self.limpiar_ventana()
        self.menu_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.menu_frame.pack(padx=20, pady=20)

        self.crear_registro_button = tk.Button(self.menu_frame, text="Crear Registro", command=self.mostrar_crear_registro, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.crear_registro_button.pack(pady=10)
        self.ver_registros_button = tk.Button(self.menu_frame, text="Ver Registros", command=self.ver_registros, bg="#2196F3", fg="white", font=("Helvetica", 12))
        self.ver_registros_button.pack(pady=10)
        self.editar_perfil_button = tk.Button(self.menu_frame, text="Editar Perfil", command=self.mostrar_editar_perfil, bg="#FF9800", fg="white", font=("Helvetica", 12))
        self.editar_perfil_button.pack(pady=10)
        self.cerrar_sesion_button = tk.Button(self.menu_frame, text="Cerrar Sesión", command=self.cerrar_sesion, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cerrar_sesion_button.pack(pady=10)

    def mostrar_crear_registro(self):
        self.limpiar_ventana()
        self.crear_registro_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.crear_registro_frame.pack(padx=20, pady=20)

        # Labels
        tk.Label(self.crear_registro_frame, text="Fecha (YYYY-MM-DD):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.crear_registro_frame, text="Duración (minutos):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.crear_registro_frame, text="Tipo de Entrenamiento:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)

        # Entries
        self.fecha_entry = tk.Entry(self.crear_registro_frame, bg="white", font=("Helvetica", 12))
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)
        self.duracion_entry = tk.Entry(self.crear_registro_frame, bg="white", font=("Helvetica", 12))
        self.duracion_entry.grid(row=1, column=1, padx=5, pady=5)
        self.tipo_entrenamiento_entry = tk.Entry(self.crear_registro_frame, bg="white", font=("Helvetica", 12))
        self.tipo_entrenamiento_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.submit_button = tk.Button(self.crear_registro_frame, text="Crear Registro", command=self.guardar_registro, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.submit_button.grid(row=3, columnspan=2, pady=10)
        self.cancel_button = tk.Button(self.crear_registro_frame, text="Cancelar", command=self.mostrar_menu, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancel_button.grid(row=4, columnspan=2, pady=10)

    def guardar_registro(self):
        fecha = self.fecha_entry.get()
        duracion = self.duracion_entry.get()
        tipo_entrenamiento = self.tipo_entrenamiento_entry.get()

        if not (fecha, duracion, tipo_entrenamiento):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            cursor = self.conexion_bd.cursor()
            cursor.execute('''INSERT INTO registros (usuario, fecha, duracion, tipo_entrenamiento)
                            VALUES (?, ?, ?, ?)''',
                            (self.usuario_actual, fecha, duracion, tipo_entrenamiento))
            self.conexion_bd.commit()
            messagebox.showinfo("Éxito", "Registro creado exitosamente.")
            self.mostrar_menu()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo crear el registro. Error: {str(e)}")

    def ver_registros(self):
        self.limpiar_ventana()
        self.ver_registros_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.ver_registros_frame.pack(padx=20, pady=20)

        cursor = self.conexion_bd.cursor()
        cursor.execute("SELECT * FROM registros WHERE usuario = ?", (self.usuario_actual,))
        registros = cursor.fetchall()

        if not registros:
            messagebox.showinfo("Información", "No hay registros disponibles.")
            self.mostrar_menu()
            return

        for idx, registro in enumerate(registros):
            tk.Label(self.ver_registros_frame, text=f"Registro {idx + 1}", bg="#f0f0f0", font=("Helvetica", 14, "bold")).grid(row=idx * 4, columnspan=2, pady=5)
            tk.Label(self.ver_registros_frame, text="Fecha:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=idx * 4 + 1, column=0, sticky="w", padx=5, pady=5)
            tk.Label(self.ver_registros_frame, text=registro[2], bg="#f0f0f0", font=("Helvetica", 12)).grid(row=idx * 4 + 1, column=1, sticky="w", padx=5, pady=5)
            tk.Label(self.ver_registros_frame, text="Duración:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=idx * 4 + 2, column=0, sticky="w", padx=5, pady=5)
            tk.Label(self.ver_registros_frame, text=registro[3], bg="#f0f0f0", font=("Helvetica", 12)).grid(row=idx * 4 + 2, column=1, sticky="w", padx=5, pady=5)
            tk.Label(self.ver_registros_frame, text="Tipo de Entrenamiento:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=idx * 4 + 3, column=0, sticky="w", padx=5, pady=5)
            tk.Label(self.ver_registros_frame, text=registro[4], bg="#f0f0f0", font=("Helvetica", 12)).grid(row=idx * 4 + 3, column=1, sticky="w", padx=5, pady=5)

        self.back_button = tk.Button(self.ver_registros_frame, text="Volver", command=self.mostrar_menu, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.back_button.grid(row=len(registros) * 4, columnspan=2, pady=10)

    def mostrar_editar_perfil(self):
        self.limpiar_ventana()
        self.editar_perfil_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.editar_perfil_frame.pack(padx=20, pady=20)

        cursor = self.conexion_bd.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (self.usuario_actual,))
        usuario_data = cursor.fetchone()

        if not usuario_data:
            messagebox.showerror("Error", "No se pudo cargar los datos del usuario.")
            self.mostrar_menu()
            return

        # Labels
        tk.Label(self.editar_perfil_frame, text="Usuario:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.editar_perfil_frame, text="Contraseña:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.editar_perfil_frame, text="Edad:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.editar_perfil_frame, text="DNI:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.editar_perfil_frame, text="Altura (cm):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.editar_perfil_frame, text="Género:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.editar_perfil_frame, text="Peso (kg):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.editar_perfil_frame, text="Grasa Corporal (%):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)

        # Entries pre-filled with current data
        self.usuario_entry = tk.Entry(self.editar_perfil_frame, bg="white", font=("Helvetica", 12))
        self.usuario_entry.grid(row=0, column=1, padx=5, pady=5)
        self.usuario_entry.insert(0, usuario_data[1])
        self.password_entry = tk.Entry(self.editar_perfil_frame, show="*", bg="white", font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_entry.insert(0, usuario_data[2])
        self.edad_entry = tk.Entry(self.editar_perfil_frame, bg="white", font=("Helvetica", 12))
        self.edad_entry.grid(row=2, column=1, padx=5, pady=5)
        self.edad_entry.insert(0, usuario_data[3])
        self.dni_entry = tk.Entry(self.editar_perfil_frame, bg="white", font=("Helvetica", 12))
        self.dni_entry.grid(row=3, column=1, padx=5, pady=5)
        self.dni_entry.insert(0, usuario_data[4])
        self.altura_entry = tk.Entry(self.editar_perfil_frame, bg="white", font=("Helvetica", 12))
        self.altura_entry.grid(row=4, column=1, padx=5, pady=5)
        self.altura_entry.insert(0, usuario_data[5])
        self.genero_combobox = ttk.Combobox(self.editar_perfil_frame, values=["Masculino", "Femenino"], state="readonly")
        self.genero_combobox.grid(row=5, column=1, padx=5, pady=5)
        self.genero_combobox.set(usuario_data[6])
        self.peso_entry = tk.Entry(self.editar_perfil_frame, bg="white", font=("Helvetica", 12))
        self.peso_entry.grid(row=6, column=1, padx=5, pady=5)
        self.peso_entry.insert(0, usuario_data[7])
        self.grasa_corporal_entry = tk.Entry(self.editar_perfil_frame, bg="white", font=("Helvetica", 12))
        self.grasa_corporal_entry.grid(row=7, column=1, padx=5, pady=5)
        self.grasa_corporal_entry.insert(0, usuario_data[8])

        # Buttons
        self.guardar_cambios_button = tk.Button(self.editar_perfil_frame, text="Guardar Cambios", command=self.guardar_cambios_perfil, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.guardar_cambios_button.grid(row=8, columnspan=2, pady=10)
        self.cancelar_button = tk.Button(self.editar_perfil_frame, text="Cancelar", command=self.mostrar_menu, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancelar_button.grid(row=9, columnspan=2, pady=10)

    def guardar_cambios_perfil(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()
        edad = self.edad_entry.get()
        dni = self.dni_entry.get()
        altura = self.altura_entry.get()
        genero = self.genero_combobox.get()
        peso = self.peso_entry.get()
        grasa_corporal = self.grasa_corporal_entry.get()

        if not (usuario and password and edad and dni and altura and genero and peso and grasa_corporal):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            cursor = self.conexion_bd.cursor()
            cursor.execute('''UPDATE usuarios SET usuario = ?, contraseña = ?, edad = ?, dni = ?, altura = ?, genero = ?, peso = ?, grasa_corporal = ?
                            WHERE usuario = ?''',
                            (usuario, password, edad, dni, altura, genero, peso, grasa_corporal, self.usuario_actual))
            self.conexion_bd.commit()
            messagebox.showinfo("Éxito", "Perfil actualizado exitosamente.")
            self.usuario_actual = usuario
            self.mostrar_menu()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo actualizar el perfil. Error: {str(e)}")

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.mostrar_inicio_sesion()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
