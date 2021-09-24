## Kijken hoe de buizen bewegen

Op dit moment zal het uitvoeren van jouw code niet veel doen. Je moet jouw functies in een lus oproepen om te zien hoe het werkt.

Op dit moment zouden deze drie regels onderaan jouw code moeten staan:

```python
matrix = gen_buizen(matrix)
matrix = afvlakken(matrix)
sense.set_pixels(matrix)
```

- In plaats van twee coderegels te gebruiken om de matrix af te vlakken en vervolgens weer te geven, kun je hiervoor een enkele regel gebruiken. Hiermee wordt voorkomen dat de werkelijke matrix elke keer wordt afgevlakt, en in plaats daarvan gebruik je gewoon een afgevlakte versie van de matrix voor de weergave. Vervang de laatste drie regels hiermee:

```python
matrix = gen_buizen(matrix)
sense.set_pixels(afvlakken(matrix))
```

- Nu kun je jouw `move_pipes (matrix)` functie-oproep toevoegen om de buizen te verplaatsen:

```python
matrix = gen_buizen(matrix)
sense.set_pixels(afvlakken(matrix))
matrix = beweeg_buizen(matrix)
```
- Hoewel dit de buizen zal verplaatsen, zullen ze niet worden weergegeven, omdat er geen tweede `set_pixels` oproep is. Om dit op te lossen, kun je gewoon een lus toevoegen zodat verplaatsen en weergeven elkaar altijd volgen.

```python
matrix = gen_buizen(matrix)
for i in range(9):
    sense.set_pixels(afvlakken(matrix))
    matrix = beweeg_buizen(matrix)
```

Probeer deze code uit te voeren en kijk wat er gebeurt. Was het een beetje snel?

- Je kunt dit oplossen door een opdracht `sleep()` toe te voegen. Bovenaan uw code importeert u de `sleep` methode uit de `time` module:

```python
from time import sleep
```

- Voeg vervolgens een opdracht `sleep` aan je lus:

```python
matrix = gen_buizen(matrix)
for i in range(9):
    sense.set_pixels(afvlakken(matrix))
    matrix = beweeg_buizen(matrix)
    sleep(1)
```

- Als je de code nu uitvoert, zou je iets meer als dit moeten zien: 
<iframe src="https://trinket.io/embed/python/e79f0007a3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>

- Een kleine wijziging geeft je een continue stroom buizen. Wijzig eenvoudig de for-lus om `3` of `4` keer te herhalen en omsluit vervolgens het hele laatste gedeelte van de code in een oneindige `while True` lus:

```python
while True:
  matrix = gen_buizen(matrix)
  for i in range(3):
      sense.set_pixels(afvlakken(matrix))
      matrix = beweeg_buizen(matrix)
      sleep(1)
```

- Dit zou je iets moeten geven dat er zo uitziet: 
<iframe src="https://trinket.io/embed/python/03d79d3f93" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>
