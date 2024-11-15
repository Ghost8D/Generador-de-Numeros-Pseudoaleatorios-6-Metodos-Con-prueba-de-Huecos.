import math
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv

def prueba_de_huecos(numeros, a, b):
    # Convertir los números a una secuencia binaria basada en el intervalo (a, b)
    secuencia_binaria = [1 if a <= numero < b else 0 for numero in numeros]

    # Encontrar los huecos
    huecos = []
    contador_huecos = 0
    contando_hueco = False

    for valor in secuencia_binaria:
        if valor == 1:
            if contando_hueco:
                huecos.append(contador_huecos)
                contador_huecos = 0
            contando_hueco = True
        elif contando_hueco:
            contador_huecos += 1
    
    if contando_hueco and contador_huecos > 0:
        huecos.append(contador_huecos)

    # Calcular frecuencias observadas y esperadas
    frecuencias_observadas = [0] * 6  # Tamaños de hueco de 0 a 5 y mayor que 5

    for hueco in huecos:
        if hueco >= 5:
            frecuencias_observadas[5] += 1
        else:
            frecuencias_observadas[hueco] += 1

    h = len(huecos)
    p_minus_a = b - a
    frecuencias_esperadas = [
        h * (p_minus_a) * ((1 - p_minus_a) ** i) for i in range(5)
    ]
    frecuencias_esperadas.append(h * ((1 - p_minus_a) ** 5) / (1 - (p_minus_a * (1 - p_minus_a))))

    # Calcular el estadístico de prueba Erros Estadisticos
    chi_cuadrado = sum(
        (obs - exp) ** 2 / exp
        for obs, exp in zip(frecuencias_observadas, frecuencias_esperadas)
        if exp > 0
    )

    # Crear ventana para mostrar resultados
    ventana_resultados = tk.Toplevel(root)
    ventana_resultados.title("Resultados - Prueba de Huecos")

    # Crear y configurar tabla para mostrar los resultados
    tree = ttk.Treeview(ventana_resultados, columns=("Tamaño del Hueco", "Frecuencia Observada", "Frecuencia Esperada"), show='headings')
    tree.heading("#1", text="Tamaño del Hueco")
    tree.heading("#2", text="Frecuencia Observada (Oi)")
    tree.heading("#3", text="Frecuencia Esperada (Ei)")

    tamaños_hueco = ["0", "1", "2", "3", "4", ">5"]

    for i in range(len(frecuencias_observadas)):
        tree.insert("", "end", values=(tamaños_hueco[i], frecuencias_observadas[i], frecuencias_esperadas[i]))

    # Añadir la fila de totales
    total_observada = sum(frecuencias_observadas)
    total_esperada = sum(frecuencias_esperadas)
    tree.insert("", "end", values=("TOTAL", total_observada, total_esperada))
    
    tree.pack()

    # Mostrar estadístico 
    label_chi_cuadrado = tk.Label(ventana_resultados, text=f"Error estadistico de prueba: {chi_cuadrado:.4f}")
    label_chi_cuadrado.pack()

def ejecutar_prueba():
    numeros_str = entrada_numeros.get("1.0", "end-1c").split()
    numeros = [float(num) for num in numeros_str]
    a = float(entrada_a.get())
    b = float(entrada_b.get())
    prueba_de_huecos(numeros, a, b)

def importar_csv():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not filepath:
        return

    numeros = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                numero = float(row[0])  # Asume que los números están en la primera columna
                numeros.append(numero)
            except ValueError:
                pass  # Ignora las filas que no contienen números válidos

    entrada_numeros.delete("1.0", tk.END)
    entrada_numeros.insert(tk.END, ' '.join(map(str, numeros)))

# Configurar la ventana principal
root = tk.Tk()
root.title("Prueba de Huecos")

# Campos de entrada para los números y los intervalos
tk.Label(root, text="Introduce los números separados por espacios o importa desde un CSV:").pack()
entrada_numeros = tk.Text(root, height=5, width=50)
entrada_numeros.pack()

tk.Button(root, text="Importar desde CSV", command=importar_csv).pack()

tk.Label(root, text="Introduce el valor de a:").pack()
entrada_a = tk.Entry(root)
entrada_a.pack()

tk.Label(root, text="Introduce el valor de b:").pack()
entrada_b = tk.Entry(root)
entrada_b.pack()

# Botón para ejecutar la prueba de huecos y mostrar los resultados
boton_prueba_huecos = tk.Button(root, text="Ejecutar Prueba de Huecos", command=ejecutar_prueba)
boton_prueba_huecos.pack()

root.mainloop()
