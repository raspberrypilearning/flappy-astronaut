## Multiple columns

- Now that you have a single column, you can make it move across the LED matrix.

- Currently the column starts on the far right of the matrix, at position `x = 7`. So to make it move, you need to use this simple algorithm.
  1. Draw a column at `x = 7` with colour red
  2. Wait half a second
  3. Draw a column at `x = 7` with colour black
  4. Draw a column at `x = 6` with colour red
  5. Keep doing this until `x = 0`
  
- You already have code that does the first part. To do the second step, you'll need to import the `sleep` method from the `time` module. Add this line to the top of your code, where you imported the `sense_hat` module.

	```python
	from time import sleep
	```

- Now, after the red column of pixels have been drawn, you can pause your program for half a second using `sleep(0.5)` and then redraw the same column using black pixels.

	```python
	from sense_hat import SenseHat
	from time import sleep
	sense = SenseHat()

	red = (255, 0, 0)
	black = (0, 0, 0)

	for y in range(8):
		sense.set_pixel(7, y, red)
	sleep(0.5)
	for y in range(8):
		sense.set_pixel(7, y, black)
	```
	
- If you run this code you should see the line of pixels being drawn and then disappearing.

- Now you need to redraw the column, but instead of using `sense.set_pixel(7, y, red)`, the `7` needs to become a `6`, and then a `5` and so on.

- You can do this using another `for` loop, and a negative step value in the `range` function. Have a look at the section below if you are unfamiliar with the `range` function.

[[[generic-python-range-function]]]

- Now, use another `for` loop, that **nests** the other two loops. It should use a `range` that produces a sequence from `7` down to `0`. You can use that variable `x` for the output of the loop, and replace `7` with `x` in your `set_pixel`.

--- hints --- --- hint ---
Your new loop should nest the other two loops.
```python
for x in range(something here):
    for y in range(8):
		sense.set_pixel(7, y, red)
	sleep(0.5)
	for y in range(8):
		sense.set_pixel(7, y, black)
```
--- /hint --- --- hint ---
The range needs to start at `7` and end at `-1` with an increment of `-1`. This will produce a sequence starting at `7` and going down to `0`.
```python
for x in range(7, -1, -1):
    for y in range(8):
		sense.set_pixel(7, y, red)
	sleep(0.5)
	for y in range(8):
		sense.set_pixel(7, y, black)
```
--- /hint --- --- hint ---
The `7` in each `set_pixel` can now be replaced with the `x`.
```python
for x in range(7, -1, -1):
    for y in range(8):
		sense.set_pixel(x, y, red)
	sleep(0.5)
	for y in range(8):
		sense.set_pixel(x, y, black)
```
<iframe src="https://trinket.io/embed/python/51ac109480" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
