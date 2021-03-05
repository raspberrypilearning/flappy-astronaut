## Representando píxeles

El Sense HAT tiene una matriz LED de 8 × 8 píxeles, y cada uno de los píxeles LED puede iluminarse en cualquier color. Esta va a ser la pantalla que usarás para mostrar tu juego Flappy Astronaut.

Cuando los programadores quieren colorear un píxel específico en una pantalla, normalmente se refieren a sus coordenadas `x` e `y`. Lo mismo es válido para la matriz LED de Sense HAT. Si quieres ver cómo las coordenadas `x` e `y` se pueden usar para establecer un píxel específico de Sense HAT, echa un vistazo a la sección a continuación.

[[[rpi-sensehat-led-coordinates]]]

- Ahora intenta configurar un solo píxel en Sense HAT. Puedes usar el siguiente código:

    ```python
    from sense_hat import SenseHat
    sense = SenseHat()

    r = (255, 0, 0)
    sense.set_pixel(0, 0, r)
    ```

- Intenta cambiar la posición del píxel que estás configurando. También intenta y cambia el color.

Si quieres configurar múltiples píxeles de esta manera, vas a necesitar muchas líneas de código. Afortunadamente, Sense HAT te permite configurar múltiples píxeles a la vez usando una **lista**. En la sección a continuación, puedes leer más sobre esto y ver algunos códigos de ejemplo.

[[[rpi-sensehat-multiple-pixels]]]

- Intenta crear una imagen usando una lista. Puedes usar este código para comenzar:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    g = (0, 255, 0)
    b = (0, 0, 0, 0)

    pixeles_creeper = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, b, b, g, g, b, b, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g,
    ]

    sense.set_ pixels(pixeles_creeper)
    ```

- Intenta crear otra imagen usando la lista. ¿Qué tal crear una carita sonriente?

El único problema con el uso de una sola lista como esta es que puede resultar complicado averiguar qué elemento de la lista corresponde a qué píxel en la pantalla. Por ejemplo, ¿cuál es el índice de la lista del píxel en `x = 5` e `y = 5`? Este puede calcularse, pero es un poco complicado.

Para solucionar este problema, los programadores a menudo usan listas bidimensionales, que también se conocen como listas de listas, para representar la distribución de píxeles en una pantalla.

Aquí hay una lista de listas simple para describir un tablero de ceros y cruces (tres-en-raya).

```python
tablero = [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         ['O', 'O', 'X']]
```

Esta es una excelente manera de representar al tablero, porque puedes usar fácilmente las coordenadas `x` e `y` para averiguar qué hay en cada uno de los cuadrados. Por ejemplo, si quieres averiguar qué carácter está en la esquina inferior izquierda, ya sabes que esta tiene una posición `x` de `0` y una posición `y` de `2` (no olvides que en Python empezamos contando elementos en una lista desde `0`).

[[[generic-python-list-index]]]

Para averiguar el carácter en esa posición, puedes escribir `tablero[y][x]`. Así que en este ejemplo sería `tablero[2][0]`.
