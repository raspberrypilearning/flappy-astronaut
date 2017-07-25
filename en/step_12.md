## Detecting a collision

- Next, you need the game to end if the flappy astronaut collides with the wall. Or, to put it another way, you want the game to continue playing, as long as the flappy astronaut makes it though the gap in the column.

- A simple function can be provided with the `x` position of the columns and the position of the gap, to determine whether the astronaut makes it though.

	```python
	def collision(x,gap):
	```

- If the `x` value of the column is 3, then the column and astronaut have the same horizontal position.

	```python
	def collision(x,gap):
		if x == 3:
	```

- Then if the `y` position of the astronaut is between `gap-1` and `gap+1`, the astronaut has made it through the gap.

	```python
	def collision(x,gap):
		if x == 3:
			if y < gap -1 or y > gap +1:
				return True
		return False
	```

- This function can be called inside the `draw_column` to see whether or not the game needs to be ended.

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
			if collision(x,gap):
				game_over = True
			x -= 1
	```
		
- Test your game to see whether it's working.

