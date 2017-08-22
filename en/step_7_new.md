## Mind the gap

- The game is going to be a little tricky, if there's no gap in the column through which the astronaut can fly, so the next step is to create a gap.

- The gap is just going to be three pixels within the column that have been coloured black. To give the player a challenge, the position of the gap within the column will be chosen at random.

- Here is what you will need to do:
   1. Assign a variable called `gap` a value that is a random number between `1` and `6` (inclusive).
   2. After the column has been drawn, set the pixel at that the at the `gap` coordinate in the column to be black.
   3. Do the same for the pixel at `gap + 1` and `gap - 1`
   
- To choose a random integer between `1` and `6`, you can use Python's `randint` method from the `random` module.

[[[generic-python-random]]]

--- hints --- --- hint ---
- Begin by importing the `randint` method, and set the `gap` variable.
```python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
red = (255, 0, 0)
black = (0, 0, 0)

gap = randint(1,6)
for x in range(7, -1, -1):
	for y in range(8):
		sense.set_pixel(x, y, red)
	sleep(0.5)
	for y in range(8):
		sense.set_pixel(x, y, black)
```
--- /hint --- --- hint ---
- With the `gap` variable set you can now use it to place a single pixel gap in the column. You can run this to see the output.
```python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
red = (255, 0, 0)
black = (0, 0, 0)

gap = randint(1,6)
for x in range(7, -1, -1):
	for y in range(8):
		sense.set_pixel(x, y, red)
	sense.set_pixel(x, gap, black)
	sleep(0.5)
	for y in range(8):
		sense.set_pixel(x, y, black)
```
--- /hint --- --- hint ---
- Finish off by also setting the pixel above and below the gap, to black.
```python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
red = (255, 0, 0)
black = (0, 0, 0)

gap = randint(1,6)
for x in range(7, -1, -1):
	for y in range(8):
		sense.set_pixel(x, y, red)
	sense.set_pixel(x, gap - 1, black)
	sense.set_pixel(x, gap, black)
	sense.set_pixel(x, gap + 1, black)
	sleep(0.5)
	for y in range(8):
		sense.set_pixel(x, y, black)
```
<iframe src="https://trinket.io/embed/python/02471e3390" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
