## Añadiendo tu astronauta

Tu astronauta estará representado por un único píxel de color. Puedes elegir el color que quieras para el astronauta, pero el ejemplo usará amarillo.

- Donde hayas establecido tus otras variables de color, ahora crea una nueva secuencia para tu color elegido de astronauta.

    ```python
    ROJO = (255, 0, 0)
    AZUL = (0, 0, 255)
    AMARILLO = (255, 255, 0)
    ```

- Como el astronauta va a ser un solo píxel, necesitará una coordenada `x` y una `y`, para que el píxel en esas coordenadas pueda ser iluminado. Cerca de donde has configurado tus colores, establece una posición `x` e `y` para el astronauta.

    ```python
    x = 0
    y = 0
    ```

El jugador va a controlar al astronauta con el joystick del Sense HAT. El joystick se puede configurar para que siempre que se utilice, envíe el **evento** a una función que has creado. Los eventos pueden ser cosas como 'presionado hasta' o 'soltar la derecha’. Para aprender cómo utilizar los eventos del módulo `SenseHat` del joystick, da una mirada a la sección de abajo.

[[[rpi-python-sensehat-joystick-event-functions]]]

- Justo encima de tu ciclo `while True`, agregar un código para que el joystick use una función (una que aún no has creado):

    ```python
    sense.stick.direction_any = dibujar_astronauta
    ```
- Ahora necesitas crear esta función `dibujar_astronauta`. Esta tendrá un único parámetro, el cual es el evento. Crea la función bajo una de tus otras funciones.

    ```python
    def dibujar_astronauta(evento):
    ```

- Esta función va a necesitar alterar las variables `x` e `y` que estableciste anteriormente para la posición del astronauta. En Python, una función no tiene normalmente permitido alterar el valor de variables que han sido declaradas fuera de la función. Para permitir que tu función `dibujar_astronauta` establezca las variables `x` e `y`, debes indicar que `x` e `y` son variables **globales**:

    ```python
    def dibujar_astronauta(evento):
        global x
        global y
    ```

- Ahora puedes iluminar el píxel en las coordenadas `x` e `y`:

    ```python
    def dibujar_astronauta(evento):
        global x
        global y
        sense.set_pixel(x, y, AMARILLO)
    ```

- El píxel se iluminará tan pronto como muevas el joystick de Sense HAT. En el emulador a continuación, puedes probarlo utilizando las teclas de cursor de tu teclado. 
<iframe src="https://trinket.io/embed/python/31c68ae6a3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>

