## Detección de bordes

Puedes notar que si tu astronauta se desvía del borde de la pantalla, tu programa se bloquea. Pruébalo si esto no te ha ocurrido todavía.

Esto sucede porque el módulo `sense_hat` arroja un error cada vez que las variables `x` o `y` van por encima de `7` o por debajo de `0`, ya que no hay LEDs en estas coordenadas.

Puedes utilizar un operador lógico para ayudar a prevenir esto. Por ejemplo, solo moverías el píxel de astronauta hacia arriba si el evento de joystick fuese `arriba` **y** la coordenada `y` es mayor que `0`.

Echa un vistazo a la sección de abajo para ver cómo utilizar los operadores lógicos Booleanos dentro de tu selección condicional.

[[[generic-python-conditional-selection-with-boolean]]]

- Ahora añade algo de detección de bordes a tu función `dibujar_astronauta`, para que los valores de coordenadas de píxeles no puedan ser menores que `0` ó mayores que `7`.

--- hints --- --- hint ---
- Debes verificar cada vez que la coordenada sea mayor que `0` antes de disminuirla, y menos de `7` antes de aumentarla. --- /hint --- --- hint ---
- Aquí está tu primer chequeo dentro de la función `dibujar_astronauta`:
  ```python
  if event.direction == "up" and y > 0:
      y -= 1
  ```
--- /hint --- --- hint ---
- Esta es la función completa:
    ```python
    def dibujar_astronauta(evento):
        global y
        global x
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
    ```
- Aquí hay un ejemplo del código completado: <iframe src="https://trinket.io/embed/python/c50810b1b0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> --- /hint --- --- /hints ---
