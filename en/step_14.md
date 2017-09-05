## Edge detection

You may notice that if your astronaut drifts off the edge of the screen, your program crashes. Try it out if this hasn't happened to you yet.

This happens because the `sense_hat` module throws an error whenever the `x` or `y` variables go above `7` or below `0`, since there are no LEDs at these coordinates.

You can use a logical operator to help prevent this. For instance, you would only move the astronaut pixel up if the joystick event was `up` **and** the `y` coordinate is greater than `0`.

Have a look at the section below to see how to use Boolean logical operators within your conditional selection.

[[[generic-python-conditional-selection-with-boolean]]]

- Now add some edge detection to your `draw_astronaut` function, so that the pixel coordinate values can't be less than `0` or greater than `7`.

--- hints --- --- hint ---
- You need to check every time that the coordinate is greater than `0` before decreasing it, and less than `7` before increasing it.
--- /hint --- --- hint ---
- Here is your first check within the `draw_astronaut` function:
  ```python
  if event.direction == "up" and y > 0:
	  y -= 1
  ```
--- /hint --- --- hint ---
- Here's the whole function:
	```python
	def draw_astronaut(event):
		global y
		global x
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
	```
- Here's an example of the completed code:
<iframe src="https://trinket.io/embed/python/c50810b1b0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
