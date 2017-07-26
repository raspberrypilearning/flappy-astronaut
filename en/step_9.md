## Threading

Now we have a single column scrolling across the matrix, but what if we wanted to display more than one column at a time? It would be possible to alter the `draw_column` function to produce more than one column, but it is easier to have the same function called several times.

The problem is that, at the moment, the program has to wait for a function to finish before it can be called again. It is possible to overcome this problem by using **threading**.

Threading allows you to call a function in a way that doesn't block the rest of your program, meaning that the `draw_column()` function can be called several times in a row.

- First you'll need the `Thread` function. At the top of your program, add in a line to import it.

	```python
	from sense_hat import SenseHat
	from time import sleep
	from random import randint
	from threading import Thread
	```
	
	**If you're using the trinket.io emulator, you'll need to stop at this point, as it doesn't yet support threading, and start working locally on your computer.**

- Now you can turn the function call in the `while` loop into a threaded function call, that will be called every two seconds:

	```python
	while not game_over:
		column = Thread(target=draw_column)
		column.start()
		sleep(2)
	```

- The problem is that now you have this while loop blocking the program, and there is still a lot to do, such as getting some user input and moving the flappy astronaut itself up and down. The solution is to place the `while` loop into a function, and have it called as another thread. Add it to a function first:

	```python
	def draw_columns():
		while not game_over:
			column = Thread(target=draw_column)
			column.start()
			sleep(2)
	```

- Then call it as a threaded function:

	```python
	columns = Thread(target=draw_columns)
	columns.start()
	```

	![scrolling](images/scrolling.gif)

- Your entire code so far should look like this:

	```python
	from sense_hat import SenseHat
	from time import sleep
	from random import randint
	from threading import Thread

	sense = SenseHat()
	sense.clear()

	##Globals
	game_over = False
	RED = (255,0,0)
	BLACK = (0,0,0)

	def draw_column():
		global game_over
		x = 7
		gap = randint(1,6)
		while x >= 0 and not game_over:
			for led in range(8):
				sense.set_pixel(x,led,RED)
			sense.set_pixel(x,gap,BLACK)
			sense.set_pixel(x,gap-1,BLACK)
			sense.set_pixel(x,gap+1,BLACK)
			sleep(0.5)
			for i in range(8):
				sense.set_pixel(x,i,BLACK)
			x -= 1

	def draw_columns():
		while not game_over:
			column = Thread(target=draw_column)
			column.start()
			sleep(2)

	columns = Thread(target=draw_columns)
	columns.start()
	```
- Save and run your program (Ctrl+s, F5) to make sure that it works.

