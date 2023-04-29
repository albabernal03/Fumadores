import threading 
import time
import random

#El siguiente problema que vamos a resolver es el de los fumadores, y para su resolución haremos uso de semáforos.

#Creamos el semaforo para los ingredientes  
papel_sem = threading.Semaphore(0) 
tabaco_sem = threading.Semaphore(0) 
filtros_sem = threading.Semaphore(0)
green_sem = threading.Semaphore(0)
cerilla_sem = threading.Semaphore(1) #El agente tiene la cerilla

def agente():
    while True:
        #El agente coloca dos ingredientes aleatorios en la mesa
        ingredientes = random.sample(['papel', 'tabaco', 'filtros', 'green'], 2) #el 2 se debe a que en el enunciado se pide que coloque dos ingredientes
        print("Agente coloca en la mesa: ", ingredientes)
        #Avisa a los fumadores de que hay nuevos ingredientes disponibles
        if 'papel' in ingredientes and 'tabaco' in ingredientes: #si en la lista ingredientes hay papel y tabaco
            filtros_sem.release() #libera el semaforo de filtros
        elif 'papel' in ingredientes and 'filtros' in ingredientes:
            tabaco_sem.release()
        elif 'papel' in ingredientes and 'green' in ingredientes:
            cerilla_sem.release()
        elif 'tabaco' in ingredientes and 'filtros' in ingredientes:
            papel_sem.release()
        elif 'tabaco' in ingredientes and 'green' in ingredientes:
            cerilla_sem.release()
        elif 'filtros' in ingredientes and 'green' in ingredientes:
            tabaco_sem.release()
        time.sleep(1)

def fumador1():
    #inicializamos un contador para saber cuantas veces ha fumado cada fumador
    contador = 0
    while True:
        #Espera a que estén disponibles el tabaco, los filtros y la cerilla
        print("Fumador 1 esperando por tabaco, filtros y cerilla")
        tabaco_sem.acquire()
        print("Fumador 1 adquirió tabaco")
        filtros_sem.acquire()
        print("Fumador 1 adquirió filtros")
        cerilla_sem.acquire()
        print("Fumador 1 adquirió cerilla")
        print("Fumador 1 está fumando")
        time.sleep(1)
        #Devuelve los ingredientes al agente
        print("Fumador 1 devuelve los ingredientes al agente")
        tabaco_sem.release()
        filtros_sem.release()
        cerilla_sem.release()
        #incrementamos el contador
        contador += 1
        print("Fumador 1 ha fumado ", contador, " veces")
        



       



