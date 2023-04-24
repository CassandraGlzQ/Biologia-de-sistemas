#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# Función para generar una red aleatoria con N nodos
def generar_red_aleatoria(N):
    red = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            red[i][j] = red[j][i] = random.randint(0, 1)
    return red

# Función para contar las autorregulaciones en una red dada
def contar_autorregulaciones(red):
    N = len(red)
    contador = 0
    for i in range(N):
        if red[i][i] == 1:
            contador += 1
    return contador

# Ejemplo de uso
N = int(input("Introduce el número de nodos: "))
red = generar_red_aleatoria(N)
print("Matriz de adyacencia de la red aleatoria:")
for fila in red:
    print(fila)
autorregulaciones = contar_autorregulaciones(red)
print("Número de autorregulaciones en la red aleatoria:", autorregulaciones)


# In[ ]:




