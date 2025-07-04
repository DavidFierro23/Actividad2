# Actividad2


Este repositorio contiene una implementación sencilla de la estructura de datos **cola** (FIFO) en Python, aplicada al registro de estudiantes en una materia con cupo limitado.
---

## Archivo

- **`actividad2.py`**: Código fuente principal. Contiene:
  1. **Clase `Student`**: Representa a un estudiante (ID y nombre).
  2. **Clase `Queue`**: Cola FIFO con operaciones básicas (`enqueue`, `dequeue`, `size`) y un límite de 30 estudiantes.
  3. **Función `main()`**: Secuencia de prueba que:
     - Registra 30 estudiantes.
     - Intenta inscribir al estudiante 31 (debe mostrar mensaje de "sin cupo").
     - Desencola dos estudiantes.
     - Vuelve a inscribir a dos nuevos alumnos y comprueba el límite.

---

## Requisito
- Python 3.6 o superior
---
Para poder correr el codigo, basta con descargar el archivo del codigo y correrlo localmente para poder comprobar que el límite de 30 estudiantes si existe
