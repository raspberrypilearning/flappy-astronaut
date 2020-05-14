## Randen detecteren

Je merkt misschien dat als je astronaut van de rand van het scherm afdrijft, je programma crasht. Probeer het uit als dit je nog niet is overkomen.

Dit gebeurt omdat de `sense_hat` module een foutmelding geeft wanneer de `x` of `y` variabelen boven `7` of onder `0`, omdat er geen LED's op deze coördinaten zijn.

Je kunt een logische operator gebruiken om dit te voorkomen. Je verplaatst de pixel van de astronaut bijvoorbeeld alleen omhoog als de joystick gebeurtenis `op` **en** de coördinaat `y` groter is dan `0`.

Bekijk het onderstaande gedeelte om te zien hoe je Booleaanse logische operatoren kunt gebruiken in jouw voorwaardelijke selectie.

[[[generic-python-conditional-selection-with-boolean]]]

- Voeg nu wat randdetectie toe aan jouw `teken_astronaut` functie, zodat de pixelcoördinaatwaarden niet minder dan `0` of groter dan `7`.

--- hints --- --- hint ---
- Je moet elke keer controleren of de coördinaat groter is dan `0` voordat je deze verlaagt en minder dan `7` voordat je deze verhoogt. --- /hint hint ---
- Hier is jouw eerste controle binnen de `teken_astronaut` functie:
  ```python
  if event.direction == "up" and y > 0:
      y -= 1
  ```
--- /hint ---
--- hint ---
- Hier is de hele functie:
    ```python
    def teken_astronaut(event):
        global y
        global x
        sense.set_pixel(x, y, BLAUW)
        if event.action == "pressed":
            if event.direction == "up" and y > 0:
                y -= 1
            elif event.direction == "down" and y < 7:
                y += 1
            elif event.direction == "right" and x < 7:
                x += 1
            elif event.direction == "left" and x > 0:
                x -= 1
        sense.set_pixel(x, y, GEEL)   
    ```
- Hier is een voorbeeld van de voltooide code: 

<iframe src="https://trinket.io/embed/python/c50810b1b0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

--- /hint --- --- /hints ---
