import tkinter as tk
from tkinter import ttk
import csv

def exportar_a_csv(nombre_archivo, datos, encabezados):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(encabezados)  # Escribir encabezados
        writer.writerows(datos)  # Escribir los datos

def calcular_productos_medios(seed1, seed2, iterations):
    resultados = []
    for i in range(iterations):
        x1 = int(seed1)
        x2 = int(seed2)
        x = x1 * x2
        x_str = str(x).zfill(8)
        middle_digits = x_str[2:6]
        random_number = int(middle_digits) / 10000
        resultados.append((i+1, x1, x2, x, middle_digits, random_number))
        seed1 = seed2
        seed2 = middle_digits
    return resultados

def mostrar_resultados_productos():
    seed1 = seed1_entry_productos.get()
    seed2 = seed2_entry_productos.get()
    iterations = int(iterations_entry_productos.get())

    resultados_productos = calcular_productos_medios(seed1, seed2, iterations)

    # Crear ventana para mostrar resultados de productos medios
    ventana_productos = tk.Toplevel(root)
    ventana_productos.title("Resultados - Productos Medios")

    # Crear y configurar tabla para mostrar los resultados
    result_tree_productos = ttk.Treeview(ventana_productos, columns=("Iteración", "X1", "X2", "X1*X2", "Dígitos medios", "Número aleatorio"))
    result_tree_productos.heading("#1", text="Iteración")
    result_tree_productos.heading("#2", text="X1")
    result_tree_productos.heading("#3", text="X2")
    result_tree_productos.heading("#4", text="X1*X2")
    result_tree_productos.heading("#5", text="Dígitos medios")
    result_tree_productos.heading("#6", text="Número aleatorio")
    result_tree_productos.pack()

    for resultado in resultados_productos:
        result_tree_productos.insert("", "end", values=resultado)

    # Botón para exportar a CSV
    export_button = ttk.Button(ventana_productos, text="Exportar a CSV", command=lambda: exportar_a_csv("tabla_resultados_productos.csv", resultados_productos, ["Iteración", "X1", "X2", "X1*X2", "Dígitos medios", "Número aleatorio"]))
    export_button.pack(pady=10)
    
    export_button_numeros = ttk.Button(ventana_productos, text="Exportar solo números pseudoaleatorios", 
                                       command=lambda: exportar_a_csv("Numeros_resultados_productos.csv", 
                                                                      [(resultado[-1],) for resultado in resultados_productos], 
                                                                      ["Número aleatorio"]))
    export_button_numeros.pack(pady=10)

def calcular_cuadrados_medios(seed, iterations):
    resultados = []
    for i in range(iterations):
        x = int(seed)
        x2 = x ** 2
        x_str = str(x)
        x2_str = str(x2).zfill(8)
        middle_digits = x2_str[2:6]
        random_number = int(middle_digits) / 10000
        resultados.append((i+1, x, x2, middle_digits, random_number))
        seed = middle_digits
    return resultados

def mostrar_resultados_cuadrados():
    seed = seed1_entry_cuadrados.get()
    iterations = int(iterations_entry_cuadrados.get())

    resultados_cuadrados = calcular_cuadrados_medios(seed, iterations)

    # Crear ventana para mostrar resultados de cuadrados medios
    ventana_cuadrados = tk.Toplevel(root)
    ventana_cuadrados.title("Resultados - Cuadrados Medios")

    # Crear y configurar tabla para mostrar los resultados
    result_tree_cuadrados = ttk.Treeview(ventana_cuadrados, columns=("Iteración", "X", "X^2", "Dígitos medios", "Número aleatorio"))
    result_tree_cuadrados.heading("#1", text="Iteración")
    result_tree_cuadrados.heading("#2", text="X")
    result_tree_cuadrados.heading("#3", text="X^2")
    result_tree_cuadrados.heading("#4", text="Dígitos medios")
    result_tree_cuadrados.heading("#5", text="Número aleatorio")
    result_tree_cuadrados.pack()

    for resultado in resultados_cuadrados:
        result_tree_cuadrados.insert("", "end", values=resultado)

    # Botón para exportar a CSV
    export_button = ttk.Button(ventana_cuadrados, text="Exportar a CSV", command=lambda: exportar_a_csv("Tabla_resultados_cuadrados.csv", resultados_cuadrados, ["Iteración", "X", "X^2", "Dígitos medios", "Número aleatorio"]))
    export_button.pack(pady=10)
    
    # Botón para exportar solo números pseudoaleatorios (última columna)
    export_button_numeros = ttk.Button(ventana_cuadrados, text="Exportar solo números pseudoaleatorios", 
                                    command=lambda: exportar_a_csv("Numeros_resultados_cuadrados.csv", 
                                                                   [(resultado[-1],) for resultado in resultados_cuadrados], 
                                                                   ["Número aleatorio"]))
    export_button_numeros.pack(pady=10)

def calcular_multiplicador_constante(seed, constant, iterations):
    resultados = []
    for i in range(iterations):
        x = int(seed)
        x = x * constant
        x_str = str(x).zfill(8)
        middle_digits = x_str[2:6]
        random_number = int(middle_digits) / 10000
        resultados.append((i+1, x, middle_digits, random_number))
        seed = middle_digits
    return resultados

def mostrar_resultados_multiplicador_constante():
    seed = seed_entry_multiplicador.get()
    constant = int(constant_entry.get())
    iterations = int(iterations_entry_multiplicador.get())

    resultados_multiplicador = calcular_multiplicador_constante(seed, constant, iterations)

    # Crear ventana para mostrar resultados del multiplicador constante
    ventana_multiplicador = tk.Toplevel(root)
    ventana_multiplicador.title("Resultados - Multiplicador Constante")

    # Crear y configurar tabla para mostrar los resultados
    result_tree_multiplicador = ttk.Treeview(ventana_multiplicador, columns=("Iteración", "X", "Dígitos medios", "Número aleatorio"))
    result_tree_multiplicador.heading("#1", text="Iteración")
    result_tree_multiplicador.heading("#2", text="X")
    result_tree_multiplicador.heading("#3", text="Dígitos medios")
    result_tree_multiplicador.heading("#4", text="Número aleatorio")
    result_tree_multiplicador.pack()

    for resultado in resultados_multiplicador:
        result_tree_multiplicador.insert("", "end", values=resultado)

    # Botón para exportar a CSV
    export_button = ttk.Button(ventana_multiplicador, text="Exportar a CSV", command=lambda: exportar_a_csv("Tabla_resultados_multiplicador.csv", resultados_multiplicador, ["Iteración", "X", "Dígitos medios", "Número aleatorio"]))
    export_button.pack(pady=10)
    
    export_button_numeros = ttk.Button(ventana_multiplicador, text="Exportar Solo números Pseudoaleatorios", 
                                       command=lambda: exportar_a_csv("Numeros_resultados_multiplicador.csv", 
                                                                      [(resultado[-1],) for resultado in resultados_multiplicador], 
                                                                      ["Número aleatorio"]))
    export_button_numeros.pack(pady=10)

def calcular_lineal_congruente(seed, a, c, m, iterations):
    resultados = []
    xn = int(seed)
    for i in range(iterations):
        xn_plus_1 = (a * xn + c) % m
        random_number = xn_plus_1 / (m-1)
        resultados.append((i+1, xn, xn_plus_1, random_number))
        xn = xn_plus_1
    return resultados

def mostrar_resultados_lineal_congruente():
    seed = seed_entry_lineal.get()
    a = int(a_entry.get())
    c = int(c_entry.get())
    m = int(m_entry.get())
    iterations = int(iterations_entry_lineal.get())

    resultados_lineal = calcular_lineal_congruente(seed, a, c, m, iterations)

    # Crear ventana para mostrar resultados del algoritmo lineal congruente
    ventana_lineal = tk.Toplevel(root)
    ventana_lineal.title("Resultados - Algoritmo Lineal Congruente")

    # Crear y configurar tabla para mostrar los resultados
    result_tree_lineal = ttk.Treeview(ventana_lineal, columns=("Iteración", "Xn", "Xn+1", "Número aleatorio"))
    result_tree_lineal.heading("#1", text="Iteración")
    result_tree_lineal.heading("#2", text="Xn")
    result_tree_lineal.heading("#3", text="Xn+1")
    result_tree_lineal.heading("#4", text="Número aleatorio")
    result_tree_lineal.pack()

    for resultado in resultados_lineal:
        result_tree_lineal.insert("", "end", values=resultado)

    # Botón para exportar a CSV
    export_button = ttk.Button(ventana_lineal, text="Exportar a CSV", command=lambda: exportar_a_csv("Tabla_resultados_lineal.csv", resultados_lineal, ["Iteración", "Xn", "Xn+1", "Número aleatorio"]))
    export_button.pack(pady=10)
    
    # Botón para exportar solo números pseudoaleatorios (última columna)
    export_button_numeros_lineal = ttk.Button(ventana_lineal, text="Exportar Solo números Pseudoaleatorios", 
                                           command=lambda: exportar_a_csv("Numeros_resultados_lineal.csv", 
                                                                          [(resultado[-1],) for resultado in resultados_lineal], 
                                                                          ["Número aleatorio"]))
    export_button_numeros_lineal.pack(pady=10)

def calcular_congruencial_multiplicativo(seed, a, m, iterations):
    resultados = []
    xn = int(seed)
    for i in range(iterations):
        xn_plus_1 = (a * xn) % m
        random_number = xn_plus_1 / (m-1)
        resultados.append((i+1, xn, xn_plus_1, random_number))
        xn = xn_plus_1
    return resultados

def mostrar_resultados_congruencial_multiplicativo():
    seed = seed_entry_multiplicativo.get()
    a = int(a_entry_multiplicativo.get())
    m = int(m_entry_multiplicativo.get())
    iterations = int(iterations_entry_multiplicativo.get())

    resultados_congruencial_multiplicativo = calcular_congruencial_multiplicativo(seed, a, m, iterations)

    # Crear ventana para mostrar resultados del algoritmo congruencial multiplicativo
    ventana_multiplicativo = tk.Toplevel(root)
    ventana_multiplicativo.title("Resultados - Algoritmo Congruencial Multiplicativo")

    # Crear y configurar tabla para mostrar los resultados
    result_tree_multiplicativo = ttk.Treeview(ventana_multiplicativo, columns=("Iteración", "Xn", "Xn+1", "Número aleatorio"))
    result_tree_multiplicativo.heading("#1", text="Iteración")
    result_tree_multiplicativo.heading("#2", text="Xn")
    result_tree_multiplicativo.heading("#3", text="Xn+1")
    result_tree_multiplicativo.heading("#4", text="Número aleatorio")
    result_tree_multiplicativo.pack()

    for resultado in resultados_congruencial_multiplicativo:
        result_tree_multiplicativo.insert("", "end", values=resultado)

    # Botón para exportar a CSV
    export_button = ttk.Button(ventana_multiplicativo, text="Exportar a CSV", command=lambda: exportar_a_csv("Tabla_resultados_congruencial_multiplicativo.csv", resultados_congruencial_multiplicativo, ["Iteración", "Xn", "Xn+1", "Número aleatorio"]))
    export_button.pack(pady=10)
    
    # Botón para exportar solo números pseudoaleatorios (última columna)
    export_button_numeros = ttk.Button(ventana_multiplicativo, text="Exportar solo números Pseudoaleatorios", 
                                       command=lambda: exportar_a_csv("Numeros_resultados_congruencial_multiplicativo.csv", 
                                                                      [(resultado[-1],) for resultado in resultados_congruencial_multiplicativo], 
                                                                      ["Número aleatorio"]))
    export_button_numeros.pack(pady=10)

def generate_sequence(X, m, n):
    sequence_X = []
    sequence_r = []
    
    for i in range(n):
        # Genera el siguiente número pseudoaleatorio
        X_next = (X[-1] + X[0]) % m
        sequence_X.append(X_next)
        
        # Calcula el valor normalizado r_i = X_i / (m - 1)
        normalized_X_next = X_next / (m - 1)
        sequence_r.append(normalized_X_next)
        
        # Actualiza las semillas iniciales
        X = X[1:] + [X_next]
    
    return sequence_X, sequence_r

def mostrar_resultados_conjuntos():
    seeds_input = seed_entry_conjuntos.get()
    m = int(m_entry_conjuntos.get())
    n = int(iterations_entry_conjuntos.get())

    X = [int(seed) for seed in seeds_input.split(',')]

    sequence_X, sequence_r = generate_sequence(X, m, n)

    ventana_conjuntos = tk.Toplevel(root)
    ventana_conjuntos.title("Resultados - Secuencia Generada")

    result_tree_conjuntos = ttk.Treeview(ventana_conjuntos, columns=("i", "X_i", "r_i"))
    result_tree_conjuntos.heading("#1", text="i")
    result_tree_conjuntos.heading("#2", text="X_i")
    result_tree_conjuntos.heading("#3", text="r_i")
    result_tree_conjuntos.pack()

    for i, (X_i, r_i) in enumerate(zip(sequence_X, sequence_r), 1):
        result_tree_conjuntos.insert("", "end", values=(i, X_i, r_i))

    # Botón para exportar a CSV
    export_button = ttk.Button(ventana_conjuntos, text="Exportar a CSV", command=lambda: exportar_a_csv("Tabla_resultados_conjuntos.csv", list(zip(range(1, n + 1), sequence_X, sequence_r)), ["i", "X_i", "r_i"]))
    export_button.pack(pady=10)
    
    # Botón para exportar solo números pseudoaleatorios (r_i)
    export_button_numeros = ttk.Button(ventana_conjuntos, text="Exportar solo números pseudoaleatorios", 
                                       command=lambda: exportar_a_csv("Numeros_resultados_conjuntos.csv", 
                                                                      [(r,) for r in sequence_r], 
                                                                      ["r_i"]))
    export_button_numeros.pack(pady=10)
    
# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Números Aleatorios")

# Ventana de Cuadrados Medios
cuadrados_frame = ttk.LabelFrame(root, text="Cuadrados Medios")
cuadrados_frame.pack(pady=10)

seed1_label_cuadrados = ttk.Label(cuadrados_frame, text="Semilla:")
seed1_label_cuadrados.grid(row=0, column=0)
seed1_entry_cuadrados = ttk.Entry(cuadrados_frame)
seed1_entry_cuadrados.grid(row=0, column=1)

iterations_label_cuadrados = ttk.Label(cuadrados_frame, text="Número de iteraciones:")
iterations_label_cuadrados.grid(row=1, column=0)
iterations_entry_cuadrados = ttk.Entry(cuadrados_frame)
iterations_entry_cuadrados.grid(row=1, column=1)

calculate_cuadrados_button = ttk.Button(cuadrados_frame, text="Calcular", command=mostrar_resultados_cuadrados)
calculate_cuadrados_button.grid(row=2, columnspan=2)

# Ventana de Productos Medios
productos_frame = ttk.LabelFrame(root, text="Productos Medios")
productos_frame.pack(pady=10)

seed1_label_productos = ttk.Label(productos_frame, text="Semilla 1:")
seed1_label_productos.grid(row=0, column=0)
seed1_entry_productos = ttk.Entry(productos_frame)
seed1_entry_productos.grid(row=0, column=1)

seed2_label_productos = ttk.Label(productos_frame, text="Semilla 2:")
seed2_label_productos.grid(row=1, column=0)
seed2_entry_productos = ttk.Entry(productos_frame)
seed2_entry_productos.grid(row=1, column=1)

iterations_label_productos = ttk.Label(productos_frame, text="Número de iteraciones:")
iterations_label_productos.grid(row=2, column=0)
iterations_entry_productos = ttk.Entry(productos_frame)
iterations_entry_productos.grid(row=2, column=1)

calculate_productos_button = ttk.Button(productos_frame, text="Calcular", command=mostrar_resultados_productos)
calculate_productos_button.grid(row=3, columnspan=2)

# Ventana del Multiplicador Constante
multiplicador_frame = ttk.LabelFrame(root, text="Multiplicador Constante")
multiplicador_frame.pack(pady=10)

seed_label_multiplicador = ttk.Label(multiplicador_frame, text="Semilla:")
seed_label_multiplicador.grid(row=0, column=0)
seed_entry_multiplicador = ttk.Entry(multiplicador_frame)
seed_entry_multiplicador.grid(row=0, column=1)

constant_label = ttk.Label(multiplicador_frame, text="Constante:")
constant_label.grid(row=1, column=0)
constant_entry = ttk.Entry(multiplicador_frame)
constant_entry.grid(row=1, column=1)

iterations_label_multiplicador = ttk.Label(multiplicador_frame, text="Número de iteraciones:")
iterations_label_multiplicador.grid(row=2, column=0)
iterations_entry_multiplicador = ttk.Entry(multiplicador_frame)
iterations_entry_multiplicador.grid(row=2, column=1)

calculate_multiplicador_button = ttk.Button(multiplicador_frame, text="Calcular", command=mostrar_resultados_multiplicador_constante)
calculate_multiplicador_button.grid(row=3, columnspan=2)

# Ventana del Algoritmo Lineal Congruente
lineal_frame = ttk.LabelFrame(root, text="Algoritmo Lineal")
lineal_frame.pack(pady=10)

seed_label_lineal = ttk.Label(lineal_frame, text="Semilla:")
seed_label_lineal.grid(row=0, column=0)
seed_entry_lineal = ttk.Entry(lineal_frame)
seed_entry_lineal.grid(row=0, column=1)

a_label = ttk.Label(lineal_frame, text="Multiplicador (a):")
a_label.grid(row=1, column=0)
a_entry = ttk.Entry(lineal_frame)
a_entry.grid(row=1, column=1)

c_label = ttk.Label(lineal_frame, text="Incremento (c):")
c_label.grid(row=2, column=0)
c_entry = ttk.Entry(lineal_frame)
c_entry.grid(row=2, column=1)

m_label = ttk.Label(lineal_frame, text="Módulo (m):")
m_label.grid(row=3, column=0)
m_entry = ttk.Entry(lineal_frame)
m_entry.grid(row=3, column=1)

iterations_label_lineal = ttk.Label(lineal_frame, text="Número de iteraciones:")
iterations_label_lineal.grid(row=4, column=0)
iterations_entry_lineal = ttk.Entry(lineal_frame)
iterations_entry_lineal.grid(row=4, column=1)

calculate_lineal_button = ttk.Button(lineal_frame, text="Calcular", command=mostrar_resultados_lineal_congruente)
calculate_lineal_button.grid(row=5, columnspan=2)

# Ventana del Algoritmo Congruencial Multiplicativo
multiplicativo_frame = ttk.LabelFrame(root, text="Algoritmo Congruencial Multiplicativo")
multiplicativo_frame.pack(pady=10)

seed_label_multiplicativo = ttk.Label(multiplicativo_frame, text="Semilla:")
seed_label_multiplicativo.grid(row=0, column=0)
seed_entry_multiplicativo = ttk.Entry(multiplicativo_frame)
seed_entry_multiplicativo.grid(row=0, column=1)

a_label_multiplicativo = ttk.Label(multiplicativo_frame, text="Multiplicador (a):")
a_label_multiplicativo.grid(row=1, column=0)
a_entry_multiplicativo = ttk.Entry(multiplicativo_frame)
a_entry_multiplicativo.grid(row=1, column=1)

m_label_multiplicativo = ttk.Label(multiplicativo_frame, text="Módulo (m):")
m_label_multiplicativo.grid(row=2, column=0)
m_entry_multiplicativo = ttk.Entry(multiplicativo_frame)
m_entry_multiplicativo.grid(row=2, column=1)

iterations_label_multiplicativo = ttk.Label(multiplicativo_frame, text="Número de iteraciones:")
iterations_label_multiplicativo.grid(row=3, column=0)
iterations_entry_multiplicativo = ttk.Entry(multiplicativo_frame)
iterations_entry_multiplicativo.grid(row=3, column=1)

calculate_multiplicativo_button = ttk.Button(multiplicativo_frame, text="Calcular", command=mostrar_resultados_congruencial_multiplicativo)
calculate_multiplicativo_button.grid(row=4, columnspan=2)

# Ventana de Secuencia Conjunta
conjuntos_frame = ttk.LabelFrame(root, text="Algoritmo Congruencial Aditivo")
conjuntos_frame.pack(pady=10)

seed_label_conjuntos = ttk.Label(conjuntos_frame, text="Semillas iniciales (separadas por comas):")
seed_label_conjuntos.grid(row=0, column=0)
seed_entry_conjuntos = ttk.Entry(conjuntos_frame)
seed_entry_conjuntos.grid(row=0, column=1)

m_label_conjuntos = ttk.Label(conjuntos_frame, text="Módulo (m):")
m_label_conjuntos.grid(row=1, column=0)
m_entry_conjuntos = ttk.Entry(conjuntos_frame)
m_entry_conjuntos.grid(row=1, column=1)

iterations_label_conjuntos = ttk.Label(conjuntos_frame, text="Número de números a generar:")
iterations_label_conjuntos.grid(row=2, column=0)
iterations_entry_conjuntos = ttk.Entry(conjuntos_frame)
iterations_entry_conjuntos.grid(row=2, column=1)

calculate_conjuntos_button = ttk.Button(conjuntos_frame, text="Calcular", command=mostrar_resultados_conjuntos)
calculate_conjuntos_button.grid(row=3, columnspan=2)

root.mainloop() 