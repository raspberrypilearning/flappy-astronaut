## Edge detection

You may notice that if your astronaut drifts off the edge of the screen, your program crashes. Try it out if this hasn't happened to you yet.

This happens because the `sense_hat` module throws an error whenever the `x` or `y` variables go above `7` or below `0`, since there are no LEDs at these coordinates.

You can use a logical operator to help prevent this. For instance, you would only move the astronaut pixel up if the joystick event was `up` **and** the `y` coordinate is greater than `0`.

Have a look at the section below to see how to use Boolean logical operators within your conditional selection.

[[[generic-python-conditional-selection-with-boolean]]]

- Now add some edge detection to your `draw_astronaut` function, so that the pixel coordinate values can't be less than `0` or greater than `7`.

--- hints ---
--- hint ---
- Here's the whole function:
	```python
	def draw_astronaut(event):
		global y
		global x
		sense.set_pixel(x, y, BLUE)
		if event.action == "pressed":
			if event.direction == "up" and y > 0:
				y -= 1
			elif event.direction == "down" and y < 7:
				y += 1
			elif event.direction == "right" and x < 7:
				x += 1
			elif event.direction == "left" and x > 0:
				x -= 1
		sense.set_pixel(x, y, YELLOW)   
	```
- Here's an example of the completed code:
	```python
	from sense_hat import SenseHat
	from random import randint
	from time import sleep

	sense = SenseHat()

	RED = (255, 0, 0)
	BLUE = (0, 0, 255)
	YELLOW = (255, 255, 0)

	x = 0
	y = 0

	matrix = [[BLUE for column in range(8)] for row in range(8)]


	def flatten(matrix):
	    flattened = [pixel for row in matrix for pixel in row]
	    return flattened


	def gen_pipes(matrix):
	    for row in matrix:
	        row[-1] = RED
	    gap = randint(1, 6)
	    matrix[gap][-1] = BLUE
	    matrix[gap - 1][-1] = BLUE
	    matrix[gap + 1][-1] = BLUE
	    return matrix


	def move_pipes(matrix):
	    for row in matrix:
	        for i in range(7):
	            row[i] = row[i + 1]
	        row[-1] = BLUE
	    return matrix


	def draw_astronaut(event):
	    global y
	    global x
	    sense.set_pixel(x, y, BLUE)
	    if event.action == "pressed":
	        if event.direction == "up" and y > 0:
	            y -= 1
	        elif event.direction == "down" and y < 7:
	            y += 1
	        elif event.direction == "right" and x < 7:
	            x += 1
	        elif event.direction == "left" and x > 0:
	            x -= 1
	    sense.set_pixel(x, y, YELLOW)


	sense.stick.direction_any = draw_astronaut

	while True:
	    matrix = gen_pipes(matrix)
	    for i in range(3):
	        sense.set_pixels(flatten(matrix))
	        matrix = move_pipes(matrix)
	        sense.set_pixel(x, y, YELLOW)
	        sleep(1)
	```
--- /hint ---
--- /hints ---

