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




