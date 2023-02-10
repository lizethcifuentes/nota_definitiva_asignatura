# programa para calcular la nota definitiva de una asignatura en la especialidad de sistemas.

print ("-----------------------------")
print ("---valor de nota definitiva--")
print ("-----------------------------")

#input
np = int(input("digite el valor de la nota procedimental: "))
nc = int(input("digite el valor de la nota cognitiva: "))
na = int(input("digite el valor de la nota actitudinal: "))
au = int(input("digite el valor de la nota autoevaluacion: "))
bi = int(input("digite el valor de la nota bimestral: "))


#processing
nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)


#output 
print("-------------------------------")
print ("---------resultados-----------")
print("-------------------------------")

print("Resultados NOTA DEFINITIVA " + str(nd))