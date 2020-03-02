## Moving the pipes

As mentioned in the section before, the algorithm to move the pipes will need to be repeated each time you want to shift the pixels left by `1`. Any code that needs to be repeated can be placed inside a function. Create this function below your `gen_pipes(matrix)` function:

```python
def move_pipes(matrix):
```
The algorithm for this function can be broken down like this:
  1. For each row in the matrix
     1. For each item in the row from `0` to `7`
     1. Set the item to be the same as the next item in the row
  1. Set the last item in the row to be `BLUE`.

- Try and complete this by yourself, and use the hints below if you need some help.

--- hints --- --- hint ---
- Within the function you can begin your for loop like this:
```python
def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
```
--- /hint --- --- hint ---
- To switch around the items, you can use their index.
```python
def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
```
--- /hint --- --- hint ---
- To finish, set the last item in each row to be `BLUE`, and then return the altered matrix.
```python
def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
        row[-1] = BLUE
    return matrix
```
--- /hint --- --- /hints ---
