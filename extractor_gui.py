import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog
import re

def resource_path(relative_path):
    """ Obtiene la ruta del archivo, tanto si se ejecuta como script o como ejecutable. """
    try:
        # PyInstaller crea una carpeta temporal para el ejecutable empaquetado
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def filtrar_correos(lista_correos, dominio):
    """ Filtra una lista de correos electrónicos para incluir solo aquellos que terminan con el dominio especificado. """
    return [correo.strip() for correo in lista_correos if correo.strip().endswith(f"@{dominio}")]

def ejecutar_filtrado():
    dominio = dominio_entry.get().strip()
    entrada_correos = correos_text.get("1.0", tk.END).strip()

    # Utilizamos una expresión regular para separar los correos por comas, espacios o saltos de línea.
    lista_correos = re.split(r'[,\s]+', entrada_correos)

    if not dominio:
        messagebox.showerror("Error", "Por favor, ingrese un dominio.")
        return

    correos_filtrados = filtrar_correos(lista_correos, dominio)
    correos_filtrados_text.delete("1.0", tk.END)
    correos_filtrados_text.insert(tk.END, "\n".join(correos_filtrados))

    messagebox.showinfo("Filtrado completado", f"Se encontraron {len(correos_filtrados)} correos con el dominio {dominio}.")

def guardar_como_txt():
    correos_filtrados = correos_filtrados_text.get("1.0", tk.END).strip()
    if not correos_filtrados:
        messagebox.showwarning("Advertencia", "No hay correos filtrados para guardar.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")],
        title="Guardar correos filtrados"
    )
    if file_path:
        with open(file_path, 'w') as file:
            file.write(correos_filtrados)
        messagebox.showinfo("Guardado exitoso", f"Los correos filtrados se han guardado en {file_path}.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Extractor de Correos Electrónicos")
ventana.geometry("600x610")
ventana.configure(bg="#f0f0f0")

# Agregar el logo a la ventana usando la función resource_path
icon_path = resource_path("logo.ico")
ventana.iconbitmap(icon_path)

# Etiqueta y entrada para el dominio
tk.Label(ventana, text="Ingrese el dominio a filtrar:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
dominio_entry = tk.Entry(ventana, font=("Arial", 12))
dominio_entry.pack(pady=5)

# Etiqueta y caja de texto para la lista de correos
tk.Label(ventana, text="Ingrese los correos electrónicos a filtrar:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
correos_text = tk.Text(ventana, height=8, font=("Arial", 10))
correos_text.pack(pady=5)

# Estilo de los botones
button_style = {
    "bg": "black",
    "fg": "white",
    "font": ("Arial", 12, "bold"),
    "activebackground": "#45a049",
    "activeforeground": "white",
    "relief": "raised",
    "bd": 3,
    "cursor": "hand2",
    "width": 20
}

# Botón para ejecutar el filtrado
ejecutar_btn = tk.Button(ventana, text="Filtrar Correos", command=ejecutar_filtrado, **button_style)
ejecutar_btn.pack(pady=10)

# Etiqueta y caja de texto para los correos filtrados
tk.Label(ventana, text="Correos Filtrados:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
correos_filtrados_text = tk.Text(ventana, height=8, font=("Arial", 10))
correos_filtrados_text.pack(pady=5)

# Botón para guardar los correos filtrados como archivo .txt
guardar_btn = tk.Button(ventana, text="Guardar como .txt", command=guardar_como_txt, **button_style)
guardar_btn.pack(pady=10)

# Footer con los derechos reservados
footer = tk.Label(ventana, text="© 2024 LennonDevlpr . Todos los derechos reservados.", bg="#f0f0f0", font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=5)

# Inicia la aplicación
ventana.mainloop()
