from sense_hat import SenseHat
from time import sleep
from random import randint
from threading import Thread

sensor = SenseHat()
sensor.clear()

## Globales
juego_terminado = False
ROJO = (255,0,0)
NEGRO = (0,0,0)
AZUL = (0,0,255)
y = 4
velocidad = +1


def dibujar_columna():
    global juego_terminado
    x = 7
    espacio = randint(2,6)
    while x > 0 and not juego_terminado:
        for led in range(8):
            sensor.set_pixel(x,led,ROJO)
        sensor.set_pixel(x,espacio, NEGRO)
        sensor.set_pixel(x,espacio-1,NEGRO)
        sensor.set_pixel(x,espacio+1,NEGRO)
        sleep(0.5)
        for i in range(8):
            sensor.set_pixel(x,i,NEGRO)
        if colision(x,espacio):
            juego_terminado = True
        x -= 1

    
def dibujar_columnas():
    while not juego_terminado:
        columna = Thread(target=dibujar_columna)
        columna.start()
        sleep(2)

def obtener_sacudon():
    global velocidad
    while not juego_terminado:
        acel = sensor.get_accelerometer_raw()
        x = round(acel['x'])
        y = round(acel['y'])
        z = round(acel['z'])
        sleep(0.01)
        if x != 0 or y != 0 or z != 1:
            velocidad = -1
        else:
            velocidad = +1

def colision(x,espacio):
    if x == 3:
        if y < espacio -1 or y > espacio +1:
            return True
    return False

        
columnas = Thread(target=dibujar_columnas)
columnas.start()

sacudon = Thread(target=obtener_sacudon)
sacudon.start()

while not juego_terminado:
    sensor.set_pixel(3,y,AZUL)
    sleep(0.1)
    sensor.set_pixel(3,y,NEGRO)
    y + = velocidad
    if y > 7:
        y = 7
    if y < 0:
        y = 0    


sacudon.join()
columnas.join()

sensor.show_message("Has perdido", text_colour=(255,0,0))
