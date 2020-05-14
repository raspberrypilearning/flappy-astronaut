## Je spel afmaken
- Er zijn maar een paar dingen die je moet doen voordat je helemaal klaar bent. Op de laatste regel moet je code invoegen om een bericht weer te geven om aan te geven dat het spel is afgelopen.

    ```python
    sense.show_message('Jij verliest')
    ```

- Wanneer jouw astronaut nu tegen de buizen botst, zou dit bericht moeten verschijnen.

- Je kunt een kleine bug in het programma opmerken. Soms kan jouw astronaut dwars door de buizen vliegen. Dit komt omdat de joystickdetectie buiten de hoofdgame-lus werkt. De joystick gebeurtenissen worden niet gesynchroniseerd met de bewegende kolommen.


- Om dit op te lossen, maak je een nieuwe variabele met de naam `game_over`en stel je deze in op `False` in de buurt van waar je jouw kleurconstanten hebt ingesteld. Deze variabele kan worden gebruikt om te bepalen wanneer het spel eindigt.

    ```python
    game_over = False
    ```

- Nu kun je je `while True` lus veranderen zodat het een `while not game_over` lus wordt:

    ```python
    while not game_over:
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

- Dan kun je van die vervelende `pauze`s afkomen door `game_over` op `True` te zetten.

    ```python
    while not game_over:
        matrix = gen_buizen(matrix)
        if check_botsing(matrix):
            game_over = True
        for i in range(3):
            matrix = beweeg_buizen(matrix)
            sense.set_pixels(afvlakken(matrix))
            sense.set_pixel(x, y, GEEL)   
            if check_botsing(matrix):
                game_over = True
            sleep(1)
    ```
- Voeg ten slotte `global game_over` aan de teken astronaut-functie, zodat bij een botsing `game_over` `True`kan worden en de hoofdgame-lus ten einde komt:

    ```python
    def teken_astronaut(event):
        global y
        global x
        global game_over
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
        if matrix[y][x] == ROOD:
            game_over = True
    ```

- Nu zou je een voltooid programma moeten hebben, en een game die je kunt spelen! Neem een kijkje in de laatste stap om ideeën op te doen over hoe je het kunt verbeteren.
