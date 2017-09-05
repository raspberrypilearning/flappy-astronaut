## Finishing your game
- There are just a couple of things to do before you're completely done. On the very last line, you should insert code to display a message to indicate that the game is over.

	```python
	sense.show_message('You lose')
	```

- Now, when your astronaut collides with the pipes, this message should scroll.

- You may notice a small bug in the program. Sometimes you can fly your astronaut straight through the pipes. This is because the joystick detection is operating outside of the main game loop.

- To fix this, create a new variable called `game_over`, and set it to `False` near where you have set your colour constants.

	```python
	game_over = False
	```

- Now you can change your `while True` loop so that it becomes a `while not game_over` loop:

	```python
	while not game_over:
		matrix = gen_pipes(matrix)
		if check_collision(matrix):
			break
		for i in range(3):
			matrix = move_pipes(matrix)
			sense.set_pixels(flatten(matrix))
			sense.set_pixel(x, y, YELLOW)   
			if check_collision(matrix):
				break
			sleep(1)
	```

- Then you can get rid of those nasty `break`s by setting `game_over` to `True`.

	```python
	while not game_over:
		matrix = gen_pipes(matrix)
		if check_collision(matrix):
			game_over = True
		for i in range(3):
			matrix = move_pipes(matrix)
			sense.set_pixels(flatten(matrix))
			sense.set_pixel(x, y, YELLOW)   
			if check_collision(matrix):
				game_over = True
			sleep(1)
	```
- Lastly, add `global game_over` to the draw astronaut function so that, if there is a collision, `game_over` can become `True`:

	```python
	def draw_astronaut(event):
		global y
		global x
		global game_over
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
		if matrix[y][x] == RED:
			game_over = True
	```

- Now you should have a finished program, and a game you can play! Have a look at the last step to get some ideas for how you can improve it.
