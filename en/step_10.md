## Adding the flappy astronaut

- The flappy astronaut will always sit horizontally on the 4th column of LEDs (position 3), but its vertical (y) values will have to change. This can be set as a global variable. As the astronaut can either be moving up or down, you can also set a global speed variable with `1` indicating that it is moving down and `-1` indicating that it is moving up. A nice blue colour would suit the astronaut as well.

	```python
	##Globals
	game_over = False
	RED = (255,0,0)
	BLACK = (0,0,0)
	BLUE = (0,0,255)
	y = 4
	speed = +1
	```

- You can start by illuminating a single LED. Add a new `while` loop to the bottom of your script:

	```python
	while not game_over:
		sense.set_pixel(3,y,BLUE)
	```

- Then make it fall:

	```python
	while not game_over:
		sense.set_pixel(3,y,BLUE)
		sleep(0.1)
		sense.set_pixel(3,y,BLACK)
		y += speed
	```

- When you run this, your program will crash, because `y` eventually reaches a value of 8, and that is off the edge of the matrix. It's simple to fix this though:

	```python
	while not game_over:
		sense.set_pixel(3,y,BLUE)
		sleep(0.1)
		sense.set_pixel(3,y,BLACK)
		y += speed
		if y > 7:
			y = 7
		elif y < 0:
			y = 0	
	```

