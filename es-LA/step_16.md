## Terminando tu juego
- Solo hay un par de cosas que hacer antes de que hayas terminado por completo. En la última línea, debes insertar código para mostrar un mensaje que indique que el juego ha terminado.

    ```python
    sensor.show_message('Perdiste')
    ```

- Ahora, cuando tu astronauta choca con las tuberías, este mensaje debería desplazarse.

- Puedes notar un pequeño error en el programa. Algunas veces puedes volar tu astronauta directamente a través de las tuberías. Esto se debe a que la detección de joystick está operando fuera del bucle principal del juego. Los eventos del joystick no están sincronizados con las columnas en movimiento.


- Para solucionar esto, crea una nueva variable llamada `juego_terminado` y configúrala a `False` cerca de donde has establecido tus constantes de color. Esta variable puede ser utilizada para controlar cuándo termina el juego.

    ```python
    juego_terminado = False
    ```

- Ahora puedes cambiar tu bucle `while True` para que se convierta en un bucle `while not juego_terminado`:

    ```python
    while not juego_terminado:
        matriz = gen_tuberias(matriz)
        if verificar_collisiones(matriz):
            break
        for i in range(3):
            matriz = mover_tuberias(matriz)
            sensor.set_pixels(aplanar(matriz))
            sensor.set_pixel(x, y, AMARILLO)   
            if verificar_collisiones(matriz):
                break
            sleep(1)
    ```

- Entonces puedes deshacerte de esos desagradables `break` configurando `juego_terminado` a `True`.

    ```python
    while not game_over:
        matrix = gen_pipes(matrix)
        if check_collision(matrix):
            game_over = True
        for i in range(3):
            matrix = move_pipes(matrix)
            sense. et_pixels(flatten(matrix))
            sentido. et_pixel(x, y, YELLOW)   
            if check_collision(matrix):
                game_over = True
            sleep(1)
    ```
- Por último, añade `global juego_terminado` a la función de dibujar astronauta de modo que, si hay una colisión, `juego_terminado` puede convertirse en `True` y el bucle principal llegará a su final:

    ```python
    def dibujar_astronauta(evento):
        global y
        global x
        global juego_terminado
        sensor.set_pixel(x, y, AZUL)
        if event.action == "pressed":
            if event.direction == "up" and y > 0:
                y -= 1
            elif event.direction == "down" and y < 7:
                y += 1
            elif event.direction == "right" and x < 7:
                x += 1
            elif event.direction == "left" and x > 0:
                x -= 1
        sensor.set_pixel(x, y, AMARILLO)
        if matrix[y][x] == ROJO:
            juego_terminado = True
    ```

- ¡Ahora deberías tener un programa terminado, y un juego que puedes jugar! Echa un vistazo al último paso para obtener algunas ideas sobre cómo puedes mejorarlo.
