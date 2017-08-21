## Drawing a column

- To begin this project you will need to draw a column of pixels on the right hand side of the Sense HAT's LED matrix. You can begin by illuminating a single pixel.

- Use the information below to set a single **red** pixel in the top right hand corner of the LED matrix.

[[[rpi-sensehat-single-pixel]]]

- With a single pixel lit, you can now use a `for` loop, to create a column of illuminated pixels.

[[[generic-python-for-loop]]]

- When you have completed this, you should see something like this on your Sense HAT, when you run your Python script.

![single column](images/SH-1.png)

--- hints --- --- hint ---
You can set your single pixel using the following code. This will set a pixel at `x = 7` and `y = 0` with a colour of `(255, 0, 0)`, which is red.
```python
from sense_hat import SenseHat
sense = SenseHat()

sense.set_pixel(7, 0, (255, 0, 0))
```
--- /hint --- --- hint ---
You can set the colour of the pixel first, to make this a little more readable.
```python
from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)

sense.set_pixel(7, 0, red)
```
--- /hint --- --- hint ---
You can now set the pixels inside a `for` loop so that the `y` position of the pixel changes from `0` to `7` each time through the loop.
```python
from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)

for y in range(8):
	sense.set_pixel(7, y, red)
```
<iframe src="https://trinket.io/embed/python/d192c65943" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
