## Representing pixels

The Sense HAT has an 8 x 8 pixel LED matrix. Each of the pixels can be illuminated, in any colour. This is going to be the screen you use to display your flappy astronaut game.

When programmers want to colour a specific pixel on a screen, they normally refer to it's `x` and `y` coordinates. The same is true of the Sense HAT's LED matrix. If you want to see how the `x` and `y` coordinates can be used to set a specific pixel, then have a look at the section below.

[[[rpi-sensehat-led-coordinates]]]

- Now try setting a single pixel on the Sense Hat. You can use the following code:

	```python
	from sense_hat import SenseHat
	sense = SenseHat()

	r = (255, 0, 0)
	sense.set_pixel(0, 0, r)
	```

- Have a go at changing the position of the pixel you are setting. Also try and change the colour.

If you want to set multiple pixels though, your going to need a lot of lines of code. Luckily, the Sense HAT let's you set multiple pixels at a time by using a **list**. You can read more about this, and see some example code below.

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
	
- Have a try at creating another image, using the list. How about creating a smiley face?

The only problem with using a single list like this, is it can be tricky to figure out which item in the list corresponds to which pixel on the screen. For instance: The pixel at `x = 5` and `y = 5`, is at which index in the list? To calculate this you would have to do the following calculation.

```
index = (y - 1) * 8 + x
```

This tells you that the index is `37`, but it's not very intuitive.

To solve this, programmers often use 2d lists, or what are sometimes known as lists of lists, to represent the arrangement of pixels on a screen.

Here is a simple list of lists to describe a noughts & crosses (tic-tac-toe) board.

```python
board = [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         ['O', 'O', 'X']]
```

What makes this an easy way of representing the board, is that you can easily use `x` and `y` coordinates to find out what is in each of the squares. For instance, if you want to find out which character is in the bottom left corner, you know that it has an `x` position of `0` and a `y` position of `2` (Don't forget that we start counting items in a list from 0).

[[[generic-python-list-index]]]

To find out the character in that position, you can just use `board[y][x]`. So in this example that would be `board[2][0]`
