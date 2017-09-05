## Mind the gaps

Now that you have a column of pixels representing a pipe on the right-hand side of the matrix, you need to insert a gap into it through which the astronaut can fly.

The gap needs to be three pixels high, and should be placed randomly in the column of red pixels.

![gap](images/SH-2.png)

You'll want the three-pixel-high gap to be centred around one of the rows between `1` and `6` (inclusive). You can use the `random` module to achieve this:

[[[generic-python-random]]]

- Here's what you need to do:
  1. Import the `randint` method at the top of your code
  1. After the for loop has ended, create a variable called `gap`, and assign a random number between `1` and `6` as its value
  1. Change the last pixel in that row of the matrix to `BLUE`
  1. Change the last pixel in row `gap - 1` to `BLUE`
  1. Change the last pixel in row `gap + 1` to `BLUE`

--- hints --- --- hint ---
- The method you need to import is the `randint` method.
```python
from random import randint
```
--- /hint --- --- hint ---
- After the for loop, choose a random value for `gap`.
```python
for row in matrix:
	row[-1] = RED
gap = randint(1, 6)
```
--- /hint --- --- hint ---
- Now set the pixels in the last column of each of the rows numbered `gap`, `gap + 1`, and `gap -1`.
```python
for row in matrix:
	row[-1] = RED
gap = randint(1, 6)
matrix[gap][-1] = BLUE
matrix[gap - 1][-1] = BLUE
matrix[gap + 1][+1] = BLUE
```
- Here's what it should look like:
<iframe src="https://trinket.io/embed/python/37ee188eb5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
