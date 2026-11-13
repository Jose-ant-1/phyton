def cargaLista():
    li = []
    for x in range(5):
        valor = int(input("Ingrse valor: "))
        li.append(valor)
    return li

def retornarMayorMenor(li):
    ma = li[0]
    me = li[0]
    for x in range(1,len(li)):
        if li[x] > ma: 
            ma = li[x]
        else:
            if li[x] < me:
                me = li[x]
    return [ma,me]

lista = cargaLista()
rango = retornarMayorMenor(lista)
print(f"El mayor elemento de la lista es {rango[0]}")
print(f"El menor elemento de la lista es {rango[1]}")
