from fumador import *
if __name__ == '__main__':
    agente = threading.Thread(target=agente)
    fumador1 = threading.Thread(target=fumador1)
    fumador2 = threading.Thread(target=fumador2)
    fumador3 = threading.Thread(target=fumador3)
    fumador4 = threading.Thread(target=fumador4)

    #Iniciamos los hilos
    agente.start()
    fumador1.start()
    fumador2.start()
    fumador3.start()
    fumador4.start()


    #Esperamos a que terminen los hilos
    agente.join()
    fumador1.join()
    fumador2.join()
    fumador3.join()
    fumador4.join()
