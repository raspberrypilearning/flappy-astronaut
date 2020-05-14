## Pixels vertegenwoordigen

De Sense HAT heeft een LED-matrix van 8 × 8 pixels en elk van de LED-pixels kan in elke kleur worden verlicht. Dit wordt het scherm dat je zult gebruiken om je Flappy Astronaut-spel weer te geven.

Wanneer programmeurs een specifieke pixel op een scherm willen kleuren, verwijzen ze normaal naar de coördinaten `x` en `y`. Hetzelfde geldt voor de LED-matrix van de Sense HAT. Als je wilt zien hoe `x` en `y` coördinaten kunnen worden gebruikt om een specifieke Sense HAT-pixel in te stellen, kijk dan in de onderstaande sectie.

[[[rpi-sensehat-led-coordinates]]]

- Probeer nu een enkele pixel in te stellen op de Sense HAT. Je kunt de volgende code gebruiken:

    ```python
    from sense_hat import SenseHat
    sense = SenseHat()

    r = (255, 0, 0)
    sense.set_pixel(0, 0, r)
    ```

- Probeer de positie van de pixel die je instelt te veranderen. Probeer ook de kleur te veranderen.

Als je op deze manier meerdere pixels wilt instellen, heb je veel coderegels nodig. Gelukkig kun je met de Sense HAT meerdere pixels tegelijk instellen met behulp van een **lijst**. In het onderstaande gedeelte kunt u hier meer over lezen en enkele voorbeeldcode bekijken.

[[[rpi-sensehat-multiple-pixels]]]

- Probeer een afbeelding te maken met behulp van een lijst. Je kunt deze code gebruiken om te beginnen:

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

- Probeer een andere afbeelding te maken met behulp van de lijst. Hoe zit het met het maken van een smiley?

Het enige probleem met het gebruik van een enkele lijst zoals deze is dat het lastig kan zijn om erachter te komen welk item in de lijst overeenkomt met welke pixel op het scherm. Wat is bijvoorbeeld de lijstindex van de pixel op `x = 5` en `y = 5`? Het kan worden berekend, maar het is een beetje lastig.

Om dit probleem te omzeilen, gebruiken programmeurs vaak tweedimensionale lijsten, ook wel lijsten met lijsten genoemd, om de rangschikking van pixels op een scherm weer te geven.

Hier is een eenvoudige lijst met lijsten om een bord met nullen en kruisen (tic-tac-toe) te beschrijven.

```python
bord = [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         ['O', 'O', 'X']]
```

Dit is een geweldige manier om het bord weer te geven, omdat je eenvoudig `x` en `y` coördinaten kunt gebruiken om erachter te komen wat er in elk van de vierkanten staat. Als je bijvoorbeeld wilt weten welk teken linksonder staat, weet je al dat het een positie van `x` van `0` en een positie van `y` van `2` (vergeet niet dat we in Python items in een lijst beginnen te tellen vanaf `0`).

[[[generic-python-list-index]]]

Om het personage in die positie te vinden, kun je gewoon `bord[y][x]`. Dus in dit voorbeeld zou dat `bord[2][0]`.
