## Moving the columns

- Next, we want to switch all those LEDs off and decrease the variable `x` by one, then let the loop carry on around. Another `for` loop can be easily used to turn off all the LEDs. Edit your function, so that it looks like this:

	```python
	def draw_column():
		global game_over
		x = 7
		while x >= 0 and not game_over:
			for led in range(8):
				sense.set_pixel(x,led,RED)
			for led in range(8):
				sense.set_pixel(x,led,BLACK)
			x -= 1
	```

- You can test this function out if you want, but you won't see much. The LEDs will switch on then off, so quickly that there'll be nothing to see. You need to ensure there is a pause between the LEDs lighting up and then turning off again. At the top of your file, import the `time` module

	```python
	from time import sleep
	```

- Then add a sleep interval between switching the LEDs on and off again.

   ```python
		def draw_column():
			global game_over
			x = 7
			while x >= 0 and not game_over:
				for led in range(8):
					sense.set_pixel(x,led,RED)
				sleep(0.5)
				for led in range(8):
					sense.set_pixel(x,led,BLACK)
				x -= 1
				
		##Testing function call
		draw_column()
   ```
		
- Save your code and then press **F5** to run it.

![column](images/column.gif)


<iframe src="https://trinket.io/embed/python/0bce675835" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


