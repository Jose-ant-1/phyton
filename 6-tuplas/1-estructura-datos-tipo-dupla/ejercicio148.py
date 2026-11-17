fechaTupla1 = (25,12,2016)
print(f"Imprimir la primera tupla: {fechaTupla1}")

fechaLista = list(fechaTupla1)
print(f"Ahora imprimimos la lista que se copió de la tupla: {fechaLista}")

fechaLista[0] = 31
print(f"Ahora imprimimos la lista modificada: {fechaLista}")

fechaTupla2 = tuple(fechaLista)

print(f"Ahora imprimimos la sesgunda tupla que se copió de la lista: {fechaTupla2}")
