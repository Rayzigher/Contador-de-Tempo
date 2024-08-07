import time

def conversor_segundos(horas, minutos, segundos):
    return (horas * 3600) + (minutos * 60) + segundos

def contador(total_segundos):
    while total_segundos > 0:
        horas, lembrete = divmod(total_segundos, 3600)
        minutos, segundos = divmod(lembrete, 60)
        formato_tempo = '{:02}:{:02}:{:02}'.format(horas, minutos, segundos)
        print(formato_tempo, end=" \r")                                                    
        time.sleep(1)
        total_segundos -= 1

    print("Tempo Esgotado")

horas = int(input("Entre com as horas: "))
minutos = int(input("Entre com os minutos: "))
segundos = int(input("Entre com os segundos: "))

# Converte tudo para segundos
total_segundos = conversor_segundos(horas, minutos, segundos)

# Inicia a contagem regressiva
contador(total_segundos)