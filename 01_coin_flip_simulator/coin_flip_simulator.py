import random 
import matplotlib.pyplot as plt

intentos_totales = 500
intentos = range(1, intentos_totales + 1)

caras = 0
cruces = 0
historial_caras = []
historial_cruces = []

historial_porcentaje_caras = []

for intento in range(intentos_totales):
    resultado= random.choice(["Cara", "Cruz"])
    
    if resultado == "Cara":
        caras += 1
        
    else:
        cruces +=1 
    #print (resultado)
    historial_caras.append(caras)
    historial_cruces.append(cruces)
    porcentaje_caras = (caras / (intento + 1))*100
    historial_porcentaje_caras.append(porcentaje_caras)
    


print(f'Obtuviste {caras} caras')
print(f'Obtuviste {cruces} cruces')

# print(historial_cruces)
# print(historial_caras)

plt.plot(intentos, historial_caras, label = "Caras")
plt.plot(intentos, historial_cruces, label = "Cruces")

plt.xlabel("Intento")
plt.ylabel("Cantidad acumulada")
plt.title("Evolución de caras y cruces")
plt.legend()

plt.show()

plt.plot(intentos,historial_porcentaje_caras, label ="Porcentaje de caras")
plt.axhline(y=50, linestyle = "--", label = "Probabilidad teórica: 50%" )

plt.xlabel("Número de lanzamientos")
plt.ylabel("Porcentaje de caras")
plt.title("Convergencia de la probabilidad")
plt.legend()
plt.show()

