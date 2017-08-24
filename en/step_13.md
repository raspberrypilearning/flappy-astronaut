## Moving the astronaut

- You can now program the pixel representing the astronaut, to move around the screen in response to the joysticks movements. The basic algorithm is as follows.
  - If the joystick is pressed:
	- change the colour to `BLUE` to "hide" the astronaut
	- if the direction is up
	  - decrease `y` b`y` `1`
	- if the direction is down
	  - increase `y` b`y` `1`
	- if the direction is right
	  - increase `x` b`y` `1`
	- if the direction is left
	  - decrease `x` b`y` `1`
	- change the colour to `YELLOW` to show the astronaut.

- To learn how to use the `sense_hat` module's joystick events, have a look at the section below.

[[[rpi-python-sensehat-joystick-event-functions]]]

- Now add some **conditional selection** to your `draw_astronaut` function, so that the pixel will move around the LED matrix when the joystick is pressed.

--- hints --- --- hint ---
- The first thing to do is to "hide" the astronaut. In other words, set the colour to `BLUE` so that it is the same as the background.
	```python
	def draw_astronaut(event):
		global y
		global x
		sense.set_pixel(x, y, BLUE)
	```
--- /hint --- --- hint ---
- You can now use conditional selection to detect particular directions and change a coordinate. For instance:
  ```python
  def draw_astronaut(event):
	  global y
	  global x
	  sense.set_pixel(x, y, BLUE)
	  if event.action == "pressed":
		  if event.direction == "up":
			  y -= 1
  ```
- Now see if you can add `elif` statements to detect other movements and set the `x` and `y` coordinates.
--- /hint --- --- hint ---
- Here's the complete function.
```python
def draw_astronaut(event):
    global y
    global x
    sense.set_pixel(x, y, BLUE)
    if event.action == "pressed":
        if event.direction == "up":
            y -= 1
        elif event.direction == "down":
            y += 1
        elif event.direction == "right":
            x += 1
        elif event.direction == "left":
            x -= 1
    sense.set_pixel(x, y, YELLOW)
- You can see it in action here - just use the cursor keys to control the astronaut. You'll notice that you can only see the astronaut when the keys are being pressed.
<iframe src="https://trinket.io/embed/python/9dc48939c7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---

- To finish off this section, you'll need to display the astronaut within your main game loop.

	```python
	while True:
	  matrix = gen_pipes(matrix)
	  for i in range(3):
		  matrix = move_pipes(matrix)
		  sense.set_pixels(flatten(matrix))
		  sense.set_pixel(x, y, YELLOW)
		  sleep(1)
	```
