from random import random
import threading
import time
import random

#método para manejo del tiempo
def recorrer_Metraje(x):
    tiempo_corriendo = random.randint(1, 7)#tiempo que recorre el circuito cada corredor
    x.dar_Relevo(tiempo_corriendo)

class Circuito_Relevo:
    def __init__(self, total_recorridos=0):
        self.locked = threading.Lock()
        self. bandera_Corredor= total_recorridos #banderaso de que ya llegó a dar relevo

    def dar_Relevo(self, espera_relevo):
        self.locked.acquire()

        try:
            self.bandera_Corredor +=1
            print(f"El corredor#{self.bandera_Corredor} ha uniciado su recorrido")#sale de su puesto
            time.sleep(espera_relevo)#competidor corriendo

        finally:
            if self.bandera_Corredor < 5:
                print(f"El corredor#{self.bandera_Corredor} dio relevo al siguiente"+"\n")#llegó a dar relevo
            else:
                print(f"El corredor#{self.bandera_Corredor} (último relevado) llegó a la meta" + "\n") #ha llegado el ultimo
                print(">>>Circuito completado<<<")
            self.locked.release()#se queda en su puesto


if __name__ == '__main__':
    print("La carrera inicia en...")
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)
    relevo = Circuito_Relevo()
    for x in range(5):
        tstart = threading.Thread(target=recorrer_Metraje, args=(relevo,))#hilo de corredor
        tstart.start()