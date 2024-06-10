#for i in range(4):
#    print(i)

#for e in range(2,9):
#    print(e)

#for z in range(2,20,8):
#    print(z)

#for letra in 'Python':
#    print(letra)

#lista = ['brócoli', 'pepino', 'pimiento']
#for i in range( len(lista) ):
#    print(i, lista[i])
##Imprime: 0 brócoli, 1 pepino, 2 pimiento
#for verdura in lista:
#   print(verdura)
##Imprime: brócoli, pepino, pimiento

#break
#for letra in "detente":
#   if letra == "n":
#       break
#   print(letra)
##Imprime: d, e, t, e

#continue
#for letra in "detente":
#   if letra == "n":
#        continue
#   print(letra)
##Imprime: d, e, t, e, t, e

x = 6

while x > 2:
    print(x)
    x -= 1
    if x == 3:
        break
    else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
        print("Sentencia final")