## Generating pipes

In Flappy Astronaut, the astronaut will have to avoid 'pipes' that sprout from the top and bottom of the matrix. The colour of the pipes is going to be red.

To begin, you can create a single column of red pixels on the right-hand side of the matrix.

![column](images/SH-1.png)

All you need to do is to set the last item in each of the lists within the matrix to be `RED` instead of `BLUE`. Below is a refresher of how to access items in a list.

[[[generic-python-list-index]]]

- You can use a for loop so that, for each list in the matrix, the last item is set to `RED`. Position this for loop so that it runs before you flatten and display the matrix. You can use the hints below to help you out if you need them.

--- hints ---
--- hint ---
- Then you set the last item in each list to `RED`.
	```python
	for row in matrix:
		row[-1] = RED
	```
- Here's what it should do:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/flappy-astronaut-step-6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise. If you see a white smiley face, click **Run** again.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/flappy-astronaut-step-6){:target="_blank"}

--- /hint ---
--- /hints ---

