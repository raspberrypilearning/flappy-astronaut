## Using 2D lists with the Sense HAT

Now you know that the best way to represent the pixels on the LED matrix is using a 2D list, let's see how this can be done with the Sense HAT.

- Open a new Python file, or use the Sense HAT emulator at [trinket.io](https://trinket.io/).

- With the first two lines of code, import the Sense HAT modules and create a `SenseHAT` object that can be used to control the LED matrix:

```python
from sense_hat import SenseHat

sense = SenseHat()
```

Then you need to create two variables that represent the pixel colours. To make this simple, you can use red and blue. If you want to learn a little more about how computers represent colours, have a look at the section below.

[[[generic-theory-colours]]]

- To store the colour information, you can use a pair of tuples, one for red and one for blue.

```python
RED = (255, 0, 0)
BLUE = (0, 0, 255)
```

- Now you are going to create a list of lists filled with the variable `BLUE`. Manually creating it would mean a lot of typing, but instead you can use a list comprehension to complete the task in a single line.

```python
matrix = [[BLUE for column in range(8)] for row in range(8)]
```

What does this code do? The section `[BLUE for column in range(8)]` creates one list with eight values of `(0, 0, 255)` inside it. Then the `for row in range(8)` part makes eight copies of that list inside another list. After running the code, you can switch over to the interpreter and type `matrix` if you want to see the result for yourself.

If you want to learn more about list comprehensions, take a look at the section below.

[[[generic-python-simple-list-comprehensions]]]

You can't use this list of lists with the Sense HAT, as its software only understands a **flat** one-dimensional list. To deal with this issue, you are going to create a function that turns 2D lists into 1D lists. You can then use this function every time the `matrix` needs to be displayed.

To flatten a 2D list into a 1D list, you can again use a list comprehension. Here's an example of how to flatten a list.

```python
flattened = [pixel for row in matrix for pixel in row]
```

What does this do? The `for row in matrix` part looks at each of the lists in the matrix, and the `for pixel in row` section looks at the individual pixels in each row of that list. These pixels are then all placed into a single list.

- You can turn this into a function to avoid having to write it out all the time. Add this to your file:

```python
def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened
```

- To flatten your matrix and then display it on the Sense HAT, you can now simply add these lines of code to the bottom of your file.

```python
matrix = flatten(matrix)
sense.set_pixels(matrix)
```
- Save and run your code. You can see an example of the code and its output in the embedded Trinket below. <iframe src="https://trinket.io/embed/python/b4c1aad6c3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>
