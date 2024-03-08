import random

palabras=['robar','asaltar','comer','saludar','brincar','bailar','correr','tomar','abrazar','pegar','enojon','nadar']

palabra = random.choice(palabras)
#print(palabra)
totalLetas = len(palabra)

respuesta = ['-' for _ in range (len(palabra)) ]  # aqui se van almacenar las letras ingresadas
salida = ' '.join(respuesta)
print(salida)

print('Adivina la palabra con ', totalLetas, ' letras')
#___________________
intentos = 0

while intentos < 3 and "-" in respuesta:
    print(" ".join(respuesta))
    letra = input("Ingresa una letra: ")
    if letra in palabras:
        for i in range(len(palabras)):
            if palabras [i] == letra:
                respuesta[i] = letra
        print("Letra correcta")
    else:
        print("Letra incorrecta,intenta de nuevo.")
        intentos += 1
if "-" in respuesta:
    print("Adivinaste la palabra:", "".join(respuesta))
else:
    print("sin intentos. La palabra era:", palabras)
# Evaluación
'''
La evaluación se hace con un bucle while, donde el usuario ingresa una letra y
se evalua si esa letra está en la palabra a adivinar.
Si la letra está, se actualiza la respuesta con la letra.
Si no, se muestra un mensaje de error.
Sólo se tendrán 3 intentos, si se acierta la palabra o se agota los intentos,
el juego termina.
En lista llamada "respuesta" se debe almacer las letras que el usuario ingrese,
 reemplazando los guiones por las letras ingresadas


Ejemplo
Adivina la palabra con 8 letras
- - - - - - - -

Ingresa una letra: a
a - - - - - - - -
Ingresa una letra: e
a - - e - - - -

ALGORITMO

1. Realizar ciclo mientras el número de intentos sea menor a 3 o la palabra no esté completa
2.      Pedirle al usuario que ingrese una letra
3.      Verificar si la letra está en la palabra
4.      Si esta la letra, Actualizar la lista llamada respuesta
5.      Si no esta la letra, mostrar mensaje de error e incrementar el número de intentos
6.      Mostrar la lista llamada respuesta (que contiene las letras ingresadas y guiones)
7. Si la palabra está completa o se agotaron los intentos, terminar el ciclo

'''
