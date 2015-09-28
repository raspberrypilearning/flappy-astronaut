from sense_hat import SenseHat
from time import sleep
from random import randint
import threading

sense = SenseHat()
sense.clear()

y = 4
game_over = False
speed = +1

def draw_block(colour):
    sense.set_pixel(3,y,colour)

def get_shake():
    global speed
    while not game_over:
        accel = sense.get_accelerometer_raw()
        x = round(accel['x'])
        y = round(accel['y'])
        z = round(accel['z'])
        sleep(0.01)
        if x != 0 or y != 0 or z != 1:
            speed = -1
        else:
            speed = +1

def draw_column():
    global game_over
    x = 7
    gap = randint(2,6)
    while x > 0 and not game_over:
        for i in range(8):
            sense.set_pixel(x,i,0,0,255)
        sense.set_pixel(x,gap,0,0,0)
        sense.set_pixel(x,gap-1,0,0,0)
        sense.set_pixel(x,gap+1,0,0,0)
        sleep(0.5)
        for i in range(8):
            sense.set_pixel(x,i,0,0,0)
        if collision(x,gap):
            game_over = True
        x -= 1

def collision(x,gap):
    if x == 3:
        if y < gap -1 or y > gap +1:
            return True
    return False
    
def draw_columns():
    while not game_over:
        column = threading.Thread(target=draw_column)
        column.start()
        sleep(4)

columns = threading.Thread(target=draw_columns)
columns.start()

sensing = threading.Thread(target=get_shake)
sensing.start()

while not game_over:
    draw_block((255,255,255))
    sleep(0.1)
    draw_block((0,0,0))
    y += speed
    if y > 7:
        y = 7
    if y < 0:
        y = 0    


sensing.join()
sense.show_message("You Lose", text_colour=(255,0,0))
