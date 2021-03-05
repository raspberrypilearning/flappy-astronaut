## Moviendo al astronauta

- Ahora puedes programar el píxel que representa al astronauta para que se mueva alrededor de la pantalla en respuesta a los movimientos del joystick utilizando **selección condicional**. El algoritmo básico dentro de tu función `dibujar_astronauta` debe hacer lo siguiente:
  - Cuando se detecta un evento de joystick:
    - cambiar el color a `AZUL` para 'ocultar' al astronauta
    - si la dirección es hacia arriba
      - decrease `y` by `1`
    - si la dirección es hacia abajo
      - increase `y` by `1`
    - si la dirección es hacia la derecha
      - increase `x` by `1`
    - si la dirección es hacia la izquierda
      - decrease `x` by `1`
    - cambia el color a `AMARILLO` para mostrar al astronauta

- Añade código a tu función `dibujar_astronauta` para que así el píxel se mueva alrededor de la matriz LED cuando se presiona el joystick.

--- hints ---
 --- hint ---
- Lo primero que hay que hacer es "ocultar" al astronauta. En otras palabras, establece su color en `AZUL` para que sea el mismo que el fondo.
    ```python
    def dibujar_astronauta(evento):
        global y
        global x
        sense.set_pixel (x, y, AZUL)
    ```
--- /hint --- --- hint ---
- Ahora puedes utilizar la selección condicional para detectar direcciones particulares y cambiar una coordenada en respuesta. Por ejemplo:
  ```python
  def dibujar_astronauta(evento):
      global y
      global x
      sense.set_pixel(x, y, AZUL)
      if event.action == "pressed":
          if event.direction == "up":
               y -= 1
  ```
- Ve si puedes añadir las sentencias `elif` para detectar otros movimientos y establecer las coordenadas `x` e `y` debidamente.
--- /hint ---
 --- hint ---
- Esta es la función completa:
  ```python
  def dibujar_astronauta(evento):
      global y      
      global x
      sense.set_pixel(x, y, AZUL)
      if event.action == "pressed":
          if event.direction == "up":
              y -= 1
          elif event.direction == "down":
              y += 1
          elif event.direction == "right":
              x += 1
          elif event.direction == "left":
              x -= 1
      sense.set_pixel(x, y, AMARILLO)
  ```
- Puedes verlo en acción aquí - sólo tienes que usar las teclas del cursor para controlar el astronauta. Notarás que solo puedes ver al astronauta cuando las teclas están siendo presionadas. 
<iframe src="https://trinket.io/embed/python/d452f9cdd4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>
--- /hint ---
--- /hints ---

- Para terminar esta sección, necesitarás mostrar al astronauta dentro de tu bucle principal de juego.

    ```python
    while True:
      matriz = gen_tuberias(matriz)
      for i in range(3):
          sense.set_pixels(aplanar(matriz))
          matriz = mover_tuberias(matriz)
          sense.set_pixel(x, y, AMARILLO) ##THIS IS THE NEW CODE
          sleep(1)
    ```
