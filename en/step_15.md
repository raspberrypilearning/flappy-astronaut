## Collisions

To finish off the game, you need to ensure that it ends whenever the astronaut collides with one of the pipes.

- Create a new function called `check_collision` that takes the `matrix` as a parameter.

	```python
	def check_collision(matrix):
	```

- Now all you need to do is check whether the astronaut's `x, y` position corresponds to a `RED` item in the matrix. If it does, you can return `True`, and if not, return `False`.

--- hints --- --- hint ---
- The astronaut's position is at `x` and `y`. So the item you need to be checking is at `matrix[y][x]`.
--- /hint --- --- hint ---
- Within your function, you'll need to use a conditional to check the item.
  ```python
  def check_collision(matrix):
	  if matrix[y][x] == RED:
  ```
--- /hint --- --- hint ---
- Here's the complete function:
  ```python
  def check_collision(matrix):
	  if matrix[y][x] == RED:
		  return True
	  else:
		  return False
  ```
--- /hint --- --- /hints ---

- Now that you are checking for a collision, you can use this conditional in you game loop. It will need to be in both the for loop and the while loop. If it returns `True`, then you can exit the loops.

```python
while True:
    matrix = gen_pipes(matrix)
    if check_collision(matrix):
        break
    for i in range(3):
        matrix = move_pipes(matrix)
        sense.set_pixels(flatten(matrix))
        sense.set_pixel(x, y, YELLOW)   
        if check_collision(matrix):
            break
        sleep(1)
```

<iframe src="https://trinket.io/embed/python/d3b08137fd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

