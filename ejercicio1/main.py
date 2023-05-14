from coctel import Shot,CoctelFrutas

coctelFrutas=CoctelFrutas()
coctelFrutas.precio=2000
cantidad=int(input("ingrese la cantidad de cocteles: "))
añejamiento=int(input("ingresa nivel de añejamiento(1-2-3) "))
print(coctelFrutas.costo(cantidad,añejamiento))


cantidadShot=int(input("ingrese la cantidad de shot: "))
shot = Shot()
shot.precio=1000


print( shot.costo(cantidadShot) )
