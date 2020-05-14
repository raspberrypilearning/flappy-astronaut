## De astronaut verplaatsen

- Je kunt nu de pixel programmeren die de astronaut representeert om over het scherm te bewegen in reactie op de bewegingen van de joystick met behulp van **voorwaardelijke selectie**. Het basisalgoritme in jouw `draw_astronaut` functie zou het volgende moeten doen:
  - Wanneer een joystick-gebeurtenis wordt gedetecteerd:
    - verander de kleur in `BLAUW` om de astronaut te 'verbergen'
    - als de richting omhoog is
      - verlagen `y` b`y` `1`
    - als de richting omlaag is
      - verhogen `y` b`y` `1`
    - als de richting rechts is
      - verhogen `x` b`y` `1`
    - als de richting links is
      - verlagen `x` b`y` `1`
    - verander de kleur in `GEEL` om de astronaut te tonen

- Voeg code toe aan jouw `draw_astronaut` functie zodat de pixel rond de LED-matrix beweegt wanneer de joystick wordt ingedrukt.

--- hints --- --- hint ---
- Het eerste wat je moet doen is de astronaut 'verbergen'. Met andere woorden, stel de kleur in op `BLAUW` zodat deze hetzelfde is als de achtergrond.
    ```python
    def teken_astronaut(event):
        global y
        global x
        sense.set_pixel(x, y, BLAUW)
    ```
--- /hint hint ---
- Je kunt nu voorwaardelijke selectie gebruiken om bepaalde richtingen te detecteren en als reactie een coördinaat te wijzigen. Bijvoorbeeld:
  ```python
  def teken_astronaut(event):
      global y
      global x
      sense.set_pixel(x, y, BLAUW)
      if event.action == "pressed":
          if event.direction == "up":
              y -= 1
  ```
- Kijk of je `elif` instructies kunt toevoegen om andere bewegingen te detecteren en de `x` en `y` coördinaten dienovereenkomstig kunt instellen. --- /hint hint ---
- Hier is de complete functie:
  ```python
  def teken_astronaut(event):
      global y
      global x
      sense.set_pixel(x, y, BLAUW)
      if event.action == "pressed":
          if event.direction == "up":
              y -= 1
          elif event.direction == "down":
              y += 1
          elif event.direction == "right":
              x += 1
          elif event.direction == "left":
              x -= 1
      sense.set_pixel(x, y, GEEL)
  ```
- Je kunt het hier in actie zien - gebruik gewoon de cursortoetsen om de astronaut te besturen. Je zult merken dat je de astronaut alleen kunt zien wanneer de toetsen worden ingedrukt. <iframe src="https://trinket.io/embed/python/9dc48939c7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> --- / hint --- --- / hints ---

- Om dit gedeelte af te sluiten, moet je de astronaut in je hoofdgame-lus weergeven.

    ```python
    while True:
      matrix = gen_buizen(matrix)
      for i in range(3):
          sense.set_pixels(afvlakken(matrix))
          matrix = beweeg_buizen(matrix)
          sense.set_pixel(x, y, GEEL) ##DIT IS DE NIEUWE CODE
          sleep(1)
    ```
