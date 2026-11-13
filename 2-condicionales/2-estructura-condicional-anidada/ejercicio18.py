totalPreguntas = int(input("Ingrese la cantidad total de preungtas para el examen: "))
totalCorrectas = int(input("Ingrese la cantidad total de preguntas contestadas correctamente: "))

total = totalCorrectas * 100 /totalPreguntas
if total >= 90:
    print("Nivel máximo")
elif total >= 75:
    print("Nivel medio")
elif total >= 50:
    print("Nivel regular")
else:
    print("Fuera de nivel")