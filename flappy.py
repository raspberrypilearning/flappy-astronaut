from sense_hat import SenseHat
from time import sleep
from random import randint
import threading

sense = SenseHat()
sense.clear()

speed = +1
y = 4

def draw_tim(colour):
    sense.set_pixel(4,y,colour)

def get_shake():
    global speed
    while True:
        accel = sense.get_accelerometer_raw()
        x = round(accel['x'])
        y = round(accel['y'])
        z = round(accel['z'])
        print(round(x),round(y),round(z))
        sleep(0.01)
        if x != 0 or y != 0 or z != 1:
            speed = -1
        else:
            speed = +1

def draw_column():
    x = 7
    gap = randint(2,6)
    while x > 0:

        for i in range(8):
            sense.set_pixel(x,i,0,0,255)
        sense.set_pixel(x,gap,0,0,0)
        sense.set_pixel(x,gap-1,0,0,0)
        sense.set_pixel(x,gap+1,0,0,0)
        sleep(1)
        for i in range(8):
            sense.set_pixel(x,i,0,0,0)
        x -= 1


def draw_columns():
    while True:
        column = threading.Thread(target=draw_column)
        column.start()
        sleep(4)

columns = threading.Thread(target=draw_columns)
columns.start()

sensing = threading.Thread(target=get_shake)
sensing.start()




while True:

    draw_tim((255,255,255))
    sleep(0.1)
    draw_tim((0,0,0))
    y += speed
    if y > 7:
        y = 7
    if y < 0:
        y = 0    

    sleep(0.1)
sensing.join()
