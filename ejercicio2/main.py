from Escuderia import Escuderia

Escuderias=[]
numeroEscuderias = int(input("Digita el numero de escuderias: "))
constadorEscuderia = 1;
nombreEscuderiaCara=None
nombreEscuderiaCara2=None

costoMayor=0

contador=1
while contador<= numeroEscuderias:
    escuderia=Escuderia()
    escuderia.nombre=input('Digite el nombre de la escuderia: ')
    escuderia.CasaMotor=input('Digite el nombre de la casa motor: ')
    escuderia.PilotoPrincipal.nombre=input('Digite el nombre del piloto: ')
    escuderia.PilotoPrincipal.salarioAnual=input('Digite el salario anual: ')
    escuderia.PilotoPrincipal.fechaNacimiento=input('Digite la fecha de nacimiento: ')
    escuderia.PilotoPrincipal.Pais=input('Digite el pais ')
    escuderia.Piloto2.nombre=input('Digite el nombre del piloto2: ')
    escuderia.Piloto2.salarioAnual=input('Digite el salario anual: ')
    escuderia.Piloto2.fechaNacimiento=input('Digite la fecha de nacimiento: ')
    escuderia.Piloto2.Pais=input('Digite el pais ')
    escuderia.costos= int(input('Ingrese los costos '))

    
   
    Escuderias.append(escuderia)   
    contador=contador+1
   
    for escuderia in Escuderias:
        if escuderia.costos > costoMayor:
            costoMayor=escuderia.costos
            nombreEscuderiaCara=escuderia.nombre
            nombreEscuderiaCara2=escuderia.Piloto2.nombre
    
print(f'Nombre piloto 1: {nombreEscuderiaCara} - Nombre piloto 2: { nombreEscuderiaCara2 }, Costo: ${costoMayor}')