## Splitting the columns.

The game would be a little tricky if each column was a solid wall of LEDs, so you need to add a gap into the column. It would be a little too easy if the gap was always in the same place, so you'll need some randomness to its placement.

- Add a line near the top of your file to get the `randint` function from `random`. This will generate random integers for you.

	```python
	from random import randint
	```

- You'll need the program to get a random integer between 1 and 6 (inclusive) and then place a gap in the line of pixels centred about that value. Don't forget, adding a gap in the column just means that you are turning off a few pixels.

	```python
	def draw_column():
		global game_over
		x = 7
		gap = randint(1,6)
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

	##Testing function call
	draw_column()
	```

- Save and run your code. Each time it is run, the gap in the column should randomly change position.

![gap](images/gap.gif)

<iframe src="https://trinket.io/embed/python/27f336c50d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

