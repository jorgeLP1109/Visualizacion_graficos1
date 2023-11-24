import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, c='blue', label='Estudiantes')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.xlabel('Matemáticas')
plt.ylabel('Ciencias')
plt.grid(True)
plt.legend()
plt.show()

# Gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones_promedio = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

x_pos = np.arange(len(materias))

plt.figure(figsize=(10, 6))
plt.bar(x_pos, calificaciones_promedio, yerr=np.transpose(errores), align='center', alpha=0.7, ecolor='black', capsize=10)
plt.xticks(x_pos, materias)
plt.title('Calificaciones Promedio con Barras de Error')
plt.xlabel('Materias')
plt.ylabel('Calificación Promedio')
plt.legend(['Barras de Error'])
plt.show()

# Histograma
plt.figure(figsize=(8, 6))
plt.hist(matematicas, bins=10, color='green', edgecolor='black')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
plt.show()
