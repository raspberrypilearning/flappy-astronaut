## Watching the pipes move

Running your code at the moment won't do much. You need to call your functions in a loop to see it working.

At the moment you should have these three lines at the bottom of your code.

	```python
	matrix = gen_pipes(matrix)
	matrix = flatten(matrix)
	sense.set_pixels(matrix)
	```

- Instead of flattening the matrix and then displaying it, you can do this in a single line. This will stop the 2D matrix being actually flattened each time, and instead just use the flattened matrix for the display. Replace those last three lines with this:

	```python
	matrix = gen_pipes(matrix)
	sense.set_pixels(flatten(matrix))
	```
	
- Now you can add in your `move_pipes(matrix)` function call to move the pipes.

	```python
	matrix = gen_pipes(matrix)
	sense.set_pixels(flatten(matrix))	
	matrix = move_pipes(matrix)	
	```
- Although this will move the pipes, they won't be displayed, as there is no second `set_pixels` call. To solve this, you can just add in a loop, so that moving and displaying always follow each other.

	```python
	matrix = gen_pipes(matrix)
	for i in range(9):
		sense.set_pixels(flatten(matrix))	
		matrix = move_pipes(matrix)
	```

- Try and run that and see what happens. Was it a little fast?

- You can solve this by adding a `sleep()`. At the top of your code import the `sleep` method from the `time` module.

	```python
	from time import sleep
	```

- Then add a sleep into your loop.

	```python
	matrix = gen_pipes(matrix)
	for i in range(9):
		sense.set_pixels(flatten(matrix))	
		matrix = move_pipes(matrix)
		sleep(1)
	```

- Now if you run the code you should see something a little more like this:

<iframe src="https://trinket.io/embed/python/e79f0007a3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>.

- Now, one small alteration will give you a continuous stream of pipes. Simple change the `for` loop to repeat `3` or `4` times, and then enclose the entire last section of code in an infinite `while True` loop.

  ```python
  while True:
	  matrix = gen_pipes(matrix)
	  for i in range(3):
		  sense.set_pixels(flatten(matrix))
		  matrix = move_pipes(matrix)
		  sleep(1)
  ```

- This should give you something that looks like this:

<iframe src="https://trinket.io/embed/python/03d79d3f93" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
