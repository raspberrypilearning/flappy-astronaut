## 2D-lijsten gebruiken met de Sense HAT

Nu weet je dat de beste manier om de pixels op de LED-matrix weer te geven, een 2D-lijst is, laten we eens kijken hoe dit kan worden gedaan met de Sense HAT.

- Open een nieuw Python-bestand of gebruik de Sense HAT-emulator op [trinket.io](https://trinket.io/).

- Importeer met de eerste twee coderegels de Sense HAT-modules en maak een `SenseHAT` object dat kan worden gebruikt om de LED-matrix te besturen:

```python
from sense_hat import SenseHat

sense = SenseHat()
```

Vervolgens moet je twee variabelen maken die de pixelkleuren vertegenwoordigen. Om dit eenvoudig te maken, kun je rood en blauw gebruiken. Als je meer wilt weten over hoe computers kleuren vertegenwoordigen, kijk dan in het onderstaande gedeelte.

[[[generic-theory-colours]]]

- Om de kleurinformatie op te slaan, kun je een paar tuples gebruiken, één voor rood en één voor blauw.

```python
ROOD = (255, 0, 0)
BLAUW = (0, 0, 255)
```

- Nu ga je een lijst met lijsten maken die zijn gevuld met de variabele `BLAUW`. Handmatig maken zou veel typen met zich meebrengen, maar in plaats daarvan kunt u een lijstbegrip gebruiken om de taak op een enkele regel te voltooien.

```python
matrix = [[BLUE for column in range(8)] for row in range(8)]
```

Wat doet deze code? De sectie `[BLUE for column in range(8)]` maakt een lijst met acht waarden van `(0, 0, 255)` erin. Dan maakt het deel `for row in range(8)` acht kopieën van die lijst in een andere lijst. Nadat je de code hebt uitgevoerd, kun je overschakelen naar de interperter en `matrix` typen als je het resultaat zelf wilt zien.

Als je meer wilt weten over lijstbegrippen, neem dan een kijkje in de onderstaande sectie.

[[[generic-python-simple-list-comprehensions]]]

Je kunt geen gebruik maken van deze lijst van lijsten met de Sense HAT, omdat de software alleen een **vlakke** eendimensionale lijst begrijpt. Om dit probleem aan te pakken, ga je een functie maken die 2D-lijsten omzet in 1D-lijsten. Je kunt dan gebruik maken van deze functie telkens wanneer de `matrix` moet worden weergegeven.

Als je een 2D-lijst wilt samenvoegen tot een 1D-lijst, kun je opnieuw een lijstbegrip gebruiken. Hier is een voorbeeld van het afvlakken van een lijst.

```python
afgevlakt = [pixel for row in matrix for pixel in row]
```

Wat doet dit? De `for row in matrix` kijkt naar elk van de lijsten in de matrix en de sectie`for pixel in row` kijkt naar de afzonderlijke pixels in elke rij van die lijst. Deze pixels worden vervolgens allemaal in één lijst geplaatst.

- Je kunt dit in een functie veranderen om te voorkomen dat je het altijd moet wegschrijven. Voeg dit toe aan jouw bestand:

```python
def afvlakken(matrix):
    afgevlakt = [pixel for row in matrix for pixel in row]
    return afgevlakt
```

- Om jouw matrix af te vlakken en vervolgens weer te geven op de Sense HAT, kun je nu eenvoudig deze coderegels onderaan jouw bestand toevoegen.

```python
matrix = afvlakken(matrix)
sense.set_pixels(matrix)
```
- Bewaar en voer je code uit. Je kunt een voorbeeld van de code en de uitvoer ervan zien in de hieronder ingesloten Trinket. 
<iframe src="https://trinket.io/embed/python/b4c1aad6c3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>
