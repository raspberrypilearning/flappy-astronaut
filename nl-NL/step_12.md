## Jouw astronaut toevoegen

Jouw astronaut wordt weergegeven door een enkele gekleurde pixel. U kunt elke gewenste kleur kiezen voor de astronaut, maar het voorbeeld gebruikt geel.

- Waar je jouw andere kleurvariabelen hebt ingesteld, maakt je nu een nieuwe tuple voor de door je gekozen astronautenkleur.

    ```python
    ROOD = (255, 0, 0)
    BLAUW = (0, 0, 255)
    GEEL = (255, 255, 0)
    ```

- Omdat de astronaut een enkele pixel wordt, heeft ze een `x` en een `y` coördinaat nodig, zodat de pixel op die coördinaten kan worden verlicht. In de buurt van waar je jouw kleuren hebt ingesteld, stel je een positie van `x` en `y` in voor de astronaut.

    ```python
    x = 0
    y = 0
    ```

De speler gaat de astronaut besturen met de joystick van de Sense HAT. De joystick kan zo worden ingesteld dat wanneer het wordt gebruikt, het een **evenement** naar een functie stuurt die je hebt gemaakt. Gebeurtenissen kunnen dingen zijn zoals 'ingedrukt' of 'goed vrijgegeven'. Om te leren hoe u de joystick gebeurtenissen van de `sensehat` module kunt gebruiken, bekijk je het onderstaande gedeelte.

[[[rpi-python-sensehat-joystick-event-functions]]]

- Net boven je `while True` lus, voeg code toe voor de joystick om een functie te gebruiken (een die je nog niet hebt gemaakt):

    ```python
    sense.stick.direction_any = teken_astronaut
    ```
- Nu moet je deze `teken_astronaut` functie maken. Het heeft een enkele parameter, wat de gebeurtenis is. Maak de functie onder een van jouw andere functies.

    ```python
    def teken_astronaut(event):
    ```

- Deze functie moet de `x` en `y` variabelen wijzigen die je eerder hebt ingesteld voor de positie van de astronaut. In Python is het normaal gesproken niet toegestaan dat een functie de waarde wijzigt van variabelen die buiten de functie zijn gedeclareerd. Om jouw `teken_astronaut` functie toe te staan om de `x` en `y` variabelen in te stellen, moet je aangeven dat `x` en `y` **globale** variabelen zijn:

    ```python
    def teken_astronaut(event):
        global x
        global y
    ```

- Nu kun je de pixel op de coördinaten `x` en `y` verlichten:

    ```python
    def teken_astronaut(event):
        global x
        global y
        sense.set_pixel(x, y, GEEL)
    ```

- De pixel wordt verlicht zodra je de joystick van de Sense HAT beweegt. In de onderstaande emulator kun je het uitproberen met de cursortoetsen van jouw toetsenbord. 
<iframe src="https://trinket.io/embed/python/a3444b6288" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>

