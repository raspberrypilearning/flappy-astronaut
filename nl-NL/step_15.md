## Botsingen

Om het spel te beëindigen, moet je ervoor zorgen dat het eindigt wanneer de astronaut tegen een van de buizen botst.

- Maak een nieuwe functie genaamd `check_collision` die de `matrix` als parameter neemt.

    ```python
    def check_botsing(matrix):
    ```

- Nu hoef je alleen nog maar te controleren of de `x, y` positie van de astronaut overeenkomt met een `ROOD` item in de matrix. Als dit het geval is, kunt u `True` retourneren en zo niet `False` retourneren.

--- hints --- --- hint ---
- De positie van de astronaut is op `x` en `y`. Het item dat je wilt controleren, is dus `matrix[y][x]`. --- /hint hint ---
- Gebruik een voorwaardelijke functie binnen jouw functie om het item te controleren.
  ```python
  def check_botsing(matrix):
      if matrix[y][x] == ROOD:
  ```
--- /hint hint ---
- Hier is de complete functie:
  ```python
  def check_botsing(matrix):
      if matrix[y][x] == ROOD:
          return True
      else:
          return False
  ```
--- / hint --- --- / hints ---

- Nu je controleert op een botsing, kan je deze voorwaardelijke gebruiken in je gamelus. Het moet zowel in de for-lus als in de while-lus zijn. Als het `True` retourneert, kun je de lussen verlaten.

```python
while True:
    matrix = gen_buizen(matrix)
    if check_botsing(matrix):
        break
    for i in range(3):
        matrix = beweeg_buizen(matrix)
        sense.set_pixels(afvlakken(matrix))
        sense.set_pixel(x, y, GEEL)   
        if check_botsing(matrix):
            break
        sleep(1)
```
 <iframe src="https://trinket.io/embed/python/d3b08137fd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>

