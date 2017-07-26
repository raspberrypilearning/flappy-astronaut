## Setting up the Sense HAT

- To begin with you'll need to open IDLE3 by clicking on **Main Menu**, **Programming**, and selecting **Python 3**. Alternatively, you could use the [Trinket.io](https://trinket.io/) for the first part of the resource, or the [Desktop Sense HAT Emulator](https://www.raspberrypi.org/blog/desktop-sense-hat-emulator/).

- Now create a new text file to write your code in `File>New File`.

- You're going to need to import some modules from the `sense_hat` package to get going, so write the following three lines into your text file to enable access to the Sense HAT and clear the LED matrix.

	```python
	from sense_hat import SenseHat
	sense = SenseHat()
	sense.clear()
	```

<iframe src="https://trinket.io/embed/python/bca5631501" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

