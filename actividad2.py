#Clase para la creacion de estudiantes.
class Student:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"

#Clase Queue que implementa una cola para gestionar estudiantes.
class Queue:
    #enqueue(student): añade un estudiante al final de la cola.
    #dequeue(): elimina y devuelve el estudiante al frente de la cola. 
    def __init__(self, max_size: int = 30):
        self.max_size = max_size
        self._data = []

    def enqueue(self, student: Student):
        if len(self._data) >= self.max_size:
            # Cuando ya hay 30 estudiantes
            print("No hay más cupo para la materia de Estructura de Datos")
        else:
            self._data.append(student)
            print(f"Registrado: {student}")

    def dequeue(self):
        if not self._data:
            print("La cola está vacía")
            return None
        estudiante = self._data.pop(0)
        print(f"Dado de baja: {estudiante}")
        return estudiante

    def size(self) -> int:
        #Devuelve el número de estudiantes actualmente en la cola.
        return len(self._data)

#Aqui hacemos la prueba de la funcionalidad de la cola
def main():
    cola = Queue(max_size=30)

    # Se usa el for para poder registrar los 30 estudiantes
    for i in range(1, 31):
        cola.enqueue(Student(i, f"Estudiante {i}"))

    print(f"\nTotal en cola tras 30 registros: {cola.size()}\n")

    # Aqui intentamos registrar el estudiante número 31
    cola.enqueue(Student(31, "Estudiante 31"))

    # Se verifica el tamaño de la cola tras el intento
    print(f"\nTotal en cola tras intento extra: {cola.size()}\n")

    # Aqui lo que hacemos es una demostración de dequeue para que se pueda ver de igual manera
    # cuando se eliminan estudiantes
    print("Ahora desencolamos dos estudiantes de la cola:")
    cola.dequeue()
    cola.dequeue()
    print(f"\nTotal en cola después de 2 bajas: {cola.size()}")

    cola.enqueue(Student(31, "Estudiante 31"))
    # Intentamos registrar nuevamente al estudiante número 31 tras la baja de dos estudiantes
    print(f"\nTotal en cola: {cola.size()}")
    cola.enqueue(Student(32, "Estudiante 32"))
    print(f"\nTotal en cola: {cola.size()}")
    # Nuevamente probabamos que no se va a poder registrar ya que se ha llegado al máximo
    cola.enqueue(Student(33, "Estudiante 33"))
    print(f"\nTotal en cola: {cola.size()}")
if __name__ == "__main__":
    main()
