## Representing pixels

The Sense HAT has an 8×8-pixel LED matrix, and each of the LED pixels can be illuminated in any colour. This is going to be the screen you will use to display your Flappy Astronaut game.

When programmers want to colour a specific pixel on a screen, they normally refer to its `x` and `y` coordinates. The same is true of the Sense HAT's LED matrix. If you want to see how `x` and `y` coordinates can be used to set a specific Sense HAT pixel, have a look at the section below.

[[[rpi-sensehat-led-coordinates]]]

- Now try setting a single pixel on the Sense HAT. You can use the following code:

	```python
	from sense_hat import SenseHat
	sense = SenseHat()

	r = (255, 0, 0)
	sense.set_pixel(0, 0, r)
	```

- Have a go at changing the position of the pixel you are setting. Also try and change the colour.

If you want to set multiple pixels in this way, you're going to need a lot of lines of code. Luckily, the Sense HAT lets you set multiple pixels at a time by using a **list**. In the section below, you can read more about this, and see some example code.

[[[rpi-sensehat-multiple-pixels]]]

- Have a go at creating an image using a list. You can use this code to begin:

	```python
	from sense_hat import SenseHat

	sense = SenseHat()

	g = (0, 255, 0)
	b = (0, 0, 0)

	creeper_pixels = [
		g, g, g, g, g, g, g, g,
		g, g, g, g, g, g, g, g,
		g, b, b, g, g, b, b, g,
		g, b, b, g, g, b, b, g,
		g, g, g, b, b, g, g, g,
		g, g, b, b, b, b, g, g,
		g, g, b, b, b, b, g, g,
		g, g, b, g, g, b, g, g
	]

	sense.set_pixels(creeper_pixels)
	```
	
- Try creating another image using the list. How about creating a smiley face?

The only problem with using a single list like this is that it can be tricky to figure out which item in the list corresponds to which pixel on the screen. For instance, what is the list index of the pixel at `x = 5` and `y = 5`? To calculate this you would have to do the following:

```
index = (y - 1) * 8 + x
```

This will tell you that the index is `37`, but that's not very easy to understand.

To get around this problem, programmers often use two-dimensional lists, which are also known as lists of lists, to represent the arrangement of pixels on a screen.

Here is a simple list of lists to describe a noughts and crosses (tic-tac-toe) board.

```python
board = [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         ['O', 'O', 'X']]
```

This is a great way to represent the board, because you can easily use `x` and `y` coordinates to find out what is in each of the squares. For instance, if you want to find out which character is in the bottom left-hand corner, you already know that it has an `x` position of `0` and a `y` position of `2` (don't forget that in Python we start counting items in a list from `0`).

[[[generic-python-list-index]]]

To find out the character in that position, you can just write`board[y][x]`. So in this example that would be `board[2][0]`.
