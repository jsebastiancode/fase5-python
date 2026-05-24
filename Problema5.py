# ---------------------------------------------------
# Programa: Control de horas semanales de recursos
# Autor: Juan Sebastian Hernandez Mancipe
# Descripción:
# Este programa calcula las horas trabajadas
# por un grupo de recursos durante la semana
# y clasifica su jornada laboral.
# ---------------------------------------------------

# Matriz con nombre y horas trabajadas de lunes a viernes
recursos = [
    ["Ana", 8, 8, 9, 8, 8],
    ["Luis", 10, 9, 8, 9, 10],
    ["Carlos", 7, 8, 7, 8, 7],
    ["Marta", 9, 9, 9, 9, 9]
]

# Función para calcular las horas semanales
def calcular_horas(recurso):

    # Guardar nombre del recurso
    nombre = recurso[0]

    # Obtener horas trabajadas
    horas = recurso[1:]

    # Calcular total de horas
    total_horas = sum(horas)

    # Clasificar jornada laboral
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    # Retornar resultados
    return nombre, total_horas, clasificacion


# Título del reporte
print("===================================")
print(" REPORTE DE HORAS SEMANALES ")
print("===================================\n")

# Recorrer la matriz
for recurso in recursos:

    # Llamar la función
    nombre, total, clasificacion = calcular_horas(recurso)

    # Mostrar resultados
    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------------")