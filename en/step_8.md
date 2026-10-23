## Create a function to make more pipes

The game would be a little easy if only one set of pipes were created. You can generate as many pipes as you like by using a function.

- Below your `flatten()` function, create a new function called `gen_pipes`:

	```python
	def gen_pipes(matrix):
	```

- Put the code you wrote to generate a set of pipes into this function. You can just add some indentation to do this. At the end of the function, you should `return` the altered `matrix`.
  ```python
  def gen_pipes(matrix):
	  for row in matrix:
		row[-1] = RED
	  gap = randint(1, 6)
	  matrix[gap][-1] = BLUE
	  matrix[gap - 1][-1] = BLUE
	  matrix[gap + 1][-1] = BLUE
	  return matrix
  ```

- Then call the function before you flatten and display the `matrix`.

	```python
	matrix = gen_pipes(matrix)
	matrix = flatten(matrix)
	sense.set_pixels(matrix)
	```

- Here's what the code should look like now:

```python
from sense_hat import SenseHat
from random import randint

sense = SenseHat()

RED = (255, 0, 0)
BLUE = (0, 0, 255)

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


matrix = gen_pipes(matrix)
matrix = flatten(matrix)
sense.set_pixels(matrix)
```

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/flappy-astronaut-step-8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise. If you see a white smiley face, click **Run** again.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/flappy-astronaut-step-8){:target="_blank"}


