## Using 2D lists with the Sense HAT

- Now you know that the best way to represent the pixels on the LED matrix is using a 2D list, let's see how this can be done with the Sense HAT.

- Open a new Python file, or use the emulator at [trinket.io](https://trinket.io/).

- The first two lines of code, just import the Sense HAT modules and create a `SenseHAT` object that can be used to control the LED matrix.

	```python
	from sense_hat import SenseHat

	sense = SenseHat()
	```

- To begin with, you need to create two variables that represent the pixel colours. To make this simple, you can use red and blue. If you want to learn a little more about how computers represent colours, then have a look at the section below.

[[[generic-theory-colours]]]

- To store the colour information, you can use a pair of tuples. One for red and one for blue.

	```python
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)
	```

- Now you are going to create a list of lists, that is filled with the variable `BLUE`. This would mean a lot of typing or copy and pasting, to manually create it, but you can use a list comprehension to complete the task in a single line.

	```python
	matrix = [[BLUE for column in range(8)] for row in range(8)]
	```

- What does this do? The section `[BLUE for column in range(8)]` creates a single list, with 8 values of `(0, 0, 255)` inside it. Then the `for row in range(8)` makes 8 copies of that list, inside another list. You can switch over to the interpreter and type `matrix` if you want to see it for yourself, after running the code.

- You can't use this list of lists with the Sense HAT yet though, as the module only understands a **flat** 1D list. To solve, this, you are going to make a function that turns 2D lists into 1D lists. You can then use this function, every time the `matrix` needs to be displayed.

- To flatten a 2D list into a 1D list, you can again use a list comprehension.

	```python
	flattened = [pixel for row in matrix for pixel in row]
	```

- What does this do? The `for row in matrix` looks at each of the lists in the matrix 2D list and the `for pixel in row` looks at the individual pixels in each row. These pixels are then all placed into a single list.

- You can turn this into a function, to save having to write it out all the time.

	```python
	def flatten(matrix):
		flattened = [pixel for row in matrix for pixel in row]
		return flattened
	```

- To flatten your matrix and then display it on the Sense HAT, you can now simply add these lines of code.

	```python
	matrix = flatten(matrix)
	sense.set_pixels(matrix)
	``` 
- Save and run your code. You can see an example of the code and out put in the embedded trinket below.

<iframe src="https://trinket.io/embed/python/b4c1aad6c3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
