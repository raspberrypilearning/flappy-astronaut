# Flappy Block

While astronauts are kept pretty busy while on the ISS, they still need to grab a few minutes of relaxation time every now and then. As there are two Raspberry Pis with Sense HATS up there with them, a little game of Flappy Block would be the perfect way to unwind after a hard day's work in zero g.

## Setting up the Sense HAT

1. To begin with you'll need to start IDLE (`Menu>Programming>Python 3 (IDLE)`).

1. Now create a new text file to write your code in (`File>New File`)

1. You're going to need to import some modules from the sense_hat package to get going, so write the following three lines into your text file that will enable access to the Sense HAT and clear the LED matrix.

	```python
	from sense_hat import SenseHat
	sense = SenseHat()
	sense.clear()
	```

## Drawing the columns

1. You can start by drawing the columns that will scroll across the LED matrix. You're going to need some loops in this game, so you'll need a way to bring the loops to a close. For this reason, you can use a *global variable* called `game_over` to keep track of whether the game is being played or has ended.

    ```python
	## GLOBALS
	game_over = False
	```

1. To begin with, you can produce a vertical line of LEDs that scroll across the screen. This can be produced using a function called `draw_column`. The function will need to be able to change the `game_over` variable, so within the funtion you need to set it as a global variable.

```python
def draw_column():
    global game_over
```

1. The column is going to start on the far right of the matrix. If you look a the diagram below, you can see that this means it will have a position on the `x` axis of 7.

1. Set the starting position of the column, in the `draw_column` function.

```python
def draw_column():
    global game_over
	x = 7
```

1. Now you need to illuminate the last column of LEDs, pause for a little bit, turn off the column of LEDs and then illuminate the next column along, by reducing the value of `x` by one. This can all be done within a `while` loop, that keeps looping until te value of x gets to 0 or the game is over.

```python
def draw_column():
    global game_over
	x = 7
	while x > 0 and not game_over:
```

1. The column of LEDs is going to be red, and to switch them off they're going to be turned black. You need to specify these variables in your `##Globals` section.

```python
##Globals
game_over = False
RED = (255,0,0)
BLACK = (0,0,0)
```

1. To illuminate all the pixels in a given column, you could write something like `sense.set_pixel(x,0,RED)` eight times, changing the 0 to 1, then 2, then 3, etc. However, this is simpler to do in a `for` loop.

```python
def draw_column():
    global game_over
	x = 7
	while x > 0 and not game_over:
	    for led in range(8):
		    sense.set_pixel(x,led,RED)
```

1. You can test out your new function, to make sure a line of LEDs are being switched on. Save your file as **flappy.py** and then press *F5* to run it. Nothing will happen at first, because you haven't *called* the function, so just switch over into the *Python Shell* and type `draw_column()`

1. Next we want to switch off all those LEDs and decrease the variable `x` by one, then let the loop carry on around. Another for loop can be easily used to turn off all the LEDs.

```python
def draw_column():
    global game_over
	x = 7
	while x >= 0 and not game_over:
	    for led in range(8):
		    sense.set_pixel(x,led,RED)
		for led in range(8):
		    sense.set_pixel(x,led,BLACK)
		x -= 1
```

1. You can test this function out if you want, but you won't see much. The LEDs will switch on then off, so quicly that there'll be nothing to see. A pause between the LEDs coming on and then off again is needed. At the top of you file, import the `time` module

```python
from time import sleep
```

1. Then add a sleep between switching the LEDs on an off again.

```python
def draw_column():
    global game_over
	x = 7
	while x > 0 and not game_over:
	    for led in range(8):
		    sense.set_pixel(x,led,RED)
		sleep(0.5)
		for led in range(8):
		    sense.set_pixel(x,led,BLACK)
		x -= 1
```
		
1. Save your code and then press *F5* to run it. Type `draw_column()` in the Python shell to see it working.

## Splitting the columns.

The game would be a little tricky if each column is a solid wall of leds, so you need to add a gap. It would be a little easy if the gap was always in the same place, so you'll need some randomness to it's placement.

1. Add a line near the top of youf file to get the `randint` function from `random`. This will generate random integers for you.

```python
from random import randint
```

1. You'll need the program to get a random integer between 2 and 6 (inclusive) and then place a gap in the line of pixels centered about that value. Don't forget, adding a gap just means turning off a few pixels.

```python
def draw_column():
    global game_over
    x = 7
    gap = randint(2,6)
    while x > 0 and not game_over:
        for led in range(8):
            sense.set_pixel(x,led,RED)
        sense.set_pixel(x,gap,BLACK)
        sense.set_pixel(x,gap-1,BLACK)
        sense.set_pixel(x,gap+1,BLACK)
        sleep(0.5)
        for i in range(8):
            sense.set_pixel(x,i,BLACK)
        x -= 1

```

1. Save and run your code, then type `draw_column()` into the interpreter, to check that it's all working.

## Multiple Columns.

1. Now that you have a single column scrolling across the matrix, you'll want keep them coming. This can be achieved with a `while` loop. Add this code to the bottom of your script.

```python
while not game_over:
    draw_column()
    sleep(2)
```

## Threading

So that has a single column scrolling across the matrix, but only one at a time. It would be possible to alter the `draw_column` function to produce more than one column, but it is easier to have the same function called several times.

The problem is that at the moment, the program has to wait for a function to finish, before it can be called again. It is possible to over come this problem by using `threading`.

`Threading` allows you to call a function in a way that doesn't block the rest of your program, meaning that the `draw_colunm()` function can be called several times in a row.

1. First you'll need the `Thread` function. At the top of your program add in a line to import it.

```python
from sense_hat import SenseHat
from time import sleep
from random import randint
from threading import Thread
```

1. Now you can turn the function call in the `while` loop into a threaded function call, that will be called every two seconds

```python
while not game_over:
    column = Thread(target=draw_column)
	column.start()
    sleep(2)
```
1. The problem is that now you have this while loop blocking the program, and there is still a lot to do, such as getting some user input and moving the *flappy block* up and down. The solution is to place the `while` loop into a function, and have it called as another thread. Add it to a function first:

```python
def draw_columns():
	while not game_over:
		column = Thread(target=draw_column)
		column.start()
		sleep(2)
```

1. Then call it as a threaded funtion.

```python
columns = Thread(target=draw_columns)
columns.start()
```

Your entire code should so far look like this.

```python
from sense_hat import SenseHat
from time import sleep
from random import randint
from threading import Thread

sense = SenseHat()
sense.clear()

##Globals
game_over = False
RED = (255,0,0)
BLACK = (0,0,0)

def draw_column():
    global game_over
    x = 7
    gap = randint(2,6)
    while x > 0 and not game_over:
        for led in range(8):
            sense.set_pixel(x,led,RED)
        sense.set_pixel(x,gap,BLACK)
        sense.set_pixel(x,gap-1,BLACK)
        sense.set_pixel(x,gap+1,BLACK)
        sleep(0.5)
        for i in range(8):
            sense.set_pixel(x,i,BLACK)
        x -= 1
    
def draw_columns():
    while not game_over:
        column = Thread(target=draw_column)
        column.start()
        sleep(2)

columns = Thread(target=draw_columns)
columns.start()
```

## Adding the flappy block

1. The flappy block will always sit horzontally on the 4th column of LEDs (position 3), but it's vertical (y) values will have to change. This can be set as a global variable. As the block can either be moving up or down, you can also set a global speed variable with `1` indicating it's moving down and `-1` indicating it's moving up.

```python
##Globals
game_over = False
RED = (255,0,0)
BLACK = (0,0,0)
y = 4
speed = +1
```

1. 
