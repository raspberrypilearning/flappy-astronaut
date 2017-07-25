## Catching user input

- The astronaut needs to move upwards when the Raspberry Pi and Sense HAT are shaken. To do this you'll need to catch the **accelerometer** readings from the Sense HAT. To do this you can make another threaded function. Add this after the `draw_columns` function. 

	```python
	def get_shake():
		global speed
		while not game_over:

	```

- The next step is to read the data from the accelerometer, and then round each of the values. The accelerometer detects changes in velocity (speed) in three directions: x, y, and z.

	```python
	def get_shake():
		global speed
		while not game_over:
			accel = sense.get_accelerometer_raw()
			x = round(accel['x'])
			y = round(accel['y'])
			z = round(accel['z'])
	```

- If the Raspberry Pi and Sense HAT are motionless and sitting flat on a surface then the values should be:

	```
	x will be 0
	y will be 0
	z will be 1
	```

- Note that z has a value of 1 because it is reading the gravitational pull of the Earth. If these values change (because the Sense HAT is being shaken), you want the speed of the astronaut to change. A simple conditional will do this:

	```python
	def get_shake():
		global speed
		while not game_over:
			accel = sense.get_accelerometer_raw()
			x = round(accel['x'])
			y = round(accel['y'])
			z = round(accel['z'])
			if x != 0 or y != 0 or z != 1:
				speed = -1
			else:
				speed = +1
	```

- Then make this function threaded, by adding these two lines.

	```python
	shake = Thread(target=get_shake)
	shake.start()
	```

- Save and run your code, and shake the Sense HAT (carefully) to see the astronaut move up and then down.

- Your script should so far look like this:

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
	BLUE = (0,0,255)
	y = 4
	speed = +1

	def draw_column():
		global game_over
		x = 7
		gap = randint(2,6)
		while x >= 0 and not game_over:
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

	columns = Thread(target=draw_columns)
	columns.start()

	shake = Thread(target=get_shake)
	shake.start()

	while not game_over:
		sense.set_pixel(3,y,BLUE)
		sleep(0.1)
		sense.set_pixel(3,y,BLACK)
		y += speed
		if y > 7:
			y = 7
		if y < 0:
			y = 0    

	```

