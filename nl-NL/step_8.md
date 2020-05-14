## Maak een functie om meer buizen te maken

Het spel zou een beetje eenvoudig zijn als er slechts één set buizen was gemaakt. Je kunt zoveel buizen genereren als je wilt met behulp van een functie.

- Maak onder je functie `afvlakken()` een nieuwe functie met de naam `gen_buizen`:

    ```python
    def gen_buizen(matrix):
    ```

- Plaats de code die je hebt geschreven om een aantal buizen te genereren in deze functie. Je kunt hiervoor gewoon een inspringing toevoegen. Aan het einde van de functie, dien je `return` de gewijzigde `matrix` aan te roepen.
  ```python
  def gen_buizen(matrix):
      for row in matrix:
        row[-1] = ROOD
      gap = randint(1, 6)
      matrix[tussenruimte][-1] = BLAUW
      matrix[tussenruimte - 1][-1] = BLAUW
      matrix[tussenruimte + 1][-1] = BLAUW
      return matrix
  ```

- Roep vervolgens de functie aan voordat je afvlakt en geef de `matrix` weer.

    ```python
    matrix = gen_buizen(matrix)
    matrix = afvlakken(matrix)
    sense.set_pixels(matrix)
    ```

- Zo ziet de code er nu uit: <iframe src="https://trinket.io/embed/python/f77f1ddd0e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>


