## Adding your astronaut

- In this game your astronaut will be represented by a single coloured pixel. The choice of colours is yours, but the examples will use yellow. Where you have set your other colour constants, now create a new tuple for your chosen colour.

	```python
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)
	YELLOW = (255, 255, 0)
	```

- As the astronaut is going to be a single pixel, she'll need an `x` and a `y` coordinate, so that the pixel at those coordinates can be illuminated. Near where you have set your colours, set an `x` and `y` position for the astronaut.

	```python
	x = 0
	y = 0
	```

- The player is going to control the astronaut with the Sense HAT's joystick. The joystick can be setup so that whenever it is used, it sends the **event** to a function you have created. Events can be things such as **pressed up** or **released right**. Just above your `while True` loop, you can set this up to use a function you have not yet created.

	```python
	sense.stick.direction_any = draw_astronaut
	```
- Now you need to create that `draw_astronaut` function. It will have a single parameter, which is the event. Anywhere, amongst your other functions, create your `draw_astronaut` function.

	```python
	def draw_astronaut(event):
	```

- Now this function is going to need to alter the `x` and `y` variables you set earlier, for the astronaut's position. In Python, a function is not normally allowed to alter the value of variables that have been declared outside of the function. To enable your `draw_astronaut` function to do this, you need to state that the `x` and `y` variables are **global** variables.

	```python
	def draw_astronaut(event):
		global x
		global y
	```

- Now you can illuminate the pixel at the `x` and `y` coordinates.

	```python
	def draw_astronaut(event):
		global x
		global y
		sense.set_pixel(x, y, YELLOW)
	```

- The pixel will be illuminated as soon as you move the Sense HAT's joystick. In the emulator below, you can do that using your keyboard's cursor keys.

<iframe src="https://trinket.io/embed/python/a3444b6288" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

