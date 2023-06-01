#Ejercicio7

Lista1 = [1,2,3,4,5,6,9,8,10]
Lista2 = [1,1,34,56,8,3,8,45]

a = set(Lista1)
b = set(Lista2)

union = list(a | b)
soloA  = list( a - b)
soloB = list(b - a)
interseccion= list(a & b)

print(f"Lista de los elementos que aparecen en las dos listas: {union}")
print(f"Lista de los elementos que aparecen en la primera lista: {soloA}")
print(f"Lista de los elementos que aparecen en la segunda lista: {soloB}")
print(f"Lista de los elementos que aparecen en ambas listas: {interseccion}")

#Carolina EM