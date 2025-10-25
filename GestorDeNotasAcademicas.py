# Lista principal donde se guardarán los cursos y notas
cursos = []

# Pila para guardar historial de cambios (últimos cambios primero)
historial = []

#################### FUNCIONES ####################

######################################
# 1. Registra un nuevo curso con su nota
######################################
def registrar_curso():
    
    nombre = input("Ingrese el nombre del curso: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    
    try:
        nota = float(input("Ingrese la nota obtenida (0-100): "))
        if nota < 0 or nota > 100:
            print("La nota debe estar entre 0 y 100.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    
    cursos.append({"nombre": nombre, "nota": nota})
    print("Curso registrado con éxito.")

######################################
# 2. Muestra todos los cursos registrados
######################################

def mostrar_cursos():
    if not cursos:
        print("No hay cursos registrados.")
        return
    print("\nCursos registrados:")
    for i, c in enumerate(cursos, start=1):
        print(f"{i}. {c['nombre']} - Nota: {c['nota']}")

######################################
# 3. Calcula el promedio general de las notas
######################################
def calcular_promedio():
    
    if not cursos:
        print("No hay cursos registrados.")
        return
    promedio = sum(c["nota"] for c in cursos) / len(cursos)
    print(f"Promedio general: {promedio:.2f}")

################################################
# Función 4: Contar cursos aprobados y reprobados
################################################
def contar_aprobados_reprobados():

    aprobados = sum(1 for c in cursos if c["nota"] >= 60)
    reprobados = len(cursos) - aprobados
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

################################################
# Función 5: Buscar curso por nombre (búsqueda lineal)
################################################
def busqueda_lineal(nombre):

    for c in cursos:
        if nombre.lower() in c["nombre"].lower():
            return c
    return None


def buscar_curso_lineal():
    nombre = input("Ingrese el nombre del curso: ").strip()
    curso = busqueda_lineal(nombre)
    if curso:
        print(f"Curso encontrado: {curso['nombre']} - Nota: {curso['nota']}")
    else:
        print("Curso no encontrado.")

################################################
# Función 6: Actualizar nota de un curso
################################################
def actualizar_nota():

    nombre = input("Ingrese el nombre del curso: ").strip()
    curso = busqueda_lineal(nombre)
    if not curso:
        print("Curso no encontrado.")
        return
    try:
        nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
        if nueva_nota < 0 or nueva_nota > 100:
            print("La nota debe estar entre 0 y 100.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    historial.append(f"Se actualizó: {curso['nombre']} - Nota anterior: {curso['nota']} -> Nueva nota: {nueva_nota}")
    curso["nota"] = nueva_nota
    print("Nota actualizada correctamente.")

################################################
# Función 7: Eliminar un curso
################################################
def eliminar_curso():

    nombre = input("Ingrese el curso a eliminar: ").strip()
    for c in cursos:
        if nombre.lower() == c["nombre"].lower():
            confirm = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()
            if confirm == "s":
                historial.append(f"Se eliminó: {c['nombre']} - Nota: {c['nota']}")
                cursos.remove(c)
                print("Curso eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return
    print("Curso no encontrado.")

################################################
# Función 8: Ordena los cursos por nota (burbuja)
################################################
def ordenar_por_nota():

    n = len(cursos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cursos[j]["nota"] < cursos[j + 1]["nota"]:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    print("Cursos ordenados por nota (descendente):")
    mostrar_cursos()

################################################
# Función 9: Ordena los cursos por nombre (inserción)
################################################
def ordenar_por_nombre():

    for i in range(1, len(cursos)):
        actual = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]["nombre"].lower() > actual["nombre"].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = actual
    print("Cursos ordenados alfabéticamente:")
    mostrar_cursos()

################################################
# Función 10: Busca un curso por nombre (requiere lista ordenada por nombre)
################################################
def busqueda_binaria():

    if not cursos:
        print("No hay cursos registrados.")
        return
    
    nombre = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    inicio = 0
    fin = len(cursos) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre_curso = cursos[medio]["nombre"].lower()
        if nombre == nombre_curso:
            print(f"Curso encontrado: {cursos[medio]['nombre']} - Nota: {cursos[medio]['nota']}")
            return
        elif nombre < nombre_curso:
            fin = medio - 1
        else:
            inicio = medio + 1
    print("Curso no encontrado (asegúrese de que la lista esté ordenada por nombre).")

################################################
# Función 11: Simula una cola de solicitudes de revisión
################################################
def simular_cola_revision():

    cola = []
    print("Ingrese curso para revisión (escriba 'fin' para terminar):")
    while True:
        curso = input("> ").strip()
        if curso.lower() == "fin":
            break
        cola.append(curso)
    print("\nProcesando solicitudes:")
    for c in cola:
        print(f"Revisando: {c}")

################################################
# Función 12: Mostrar historial de cambios (pila)
################################################
def mostrar_historial():

    if not historial:
        print("No hay cambios registrados.")
        return
    print("Historial de cambios recientes:")
    for i, h in enumerate(reversed(historial), start=1):
        print(f"{i}. {h}")


#################### MENÚ PRINCIPAL ####################

def menu():
    while True:
        print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (búsqueda lineal)")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (burbuja)")
        print("9. Ordenar cursos por nombre (inserción)")
        print("10. Buscar curso por nombre (búsqueda binaria)")
        print("11. Simular cola de solicitudes de revisión")
        print("12. Mostrar historial de cambios (pila)")
        print("13. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1": registrar_curso()
        elif opcion == "2": mostrar_cursos()
        elif opcion == "3": calcular_promedio()
        elif opcion == "4": contar_aprobados_reprobados()
        elif opcion == "5": buscar_curso_lineal()
        elif opcion == "6": actualizar_nota()
        elif opcion == "7": eliminar_curso()
        elif opcion == "8": ordenar_por_nota()
        elif opcion == "9": ordenar_por_nombre()
        elif opcion == "10": busqueda_binaria()
        elif opcion == "11": simular_cola_revision()
        elif opcion == "12": mostrar_historial()
        elif opcion == "13":
            print("Gracias por usar el Gestor de Notas Académicas. Hasta pronto.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# ----------- EJECUCIÓN DEL PROGRAMA ----------- #
menu()
