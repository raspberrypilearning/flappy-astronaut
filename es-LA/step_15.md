## Colisiones

Para terminar el juego, debes asegurarte de que termina siempre que el astronauta choca con una de las tuberías.

- Crea una nueva función llamada `verificar_collisiones` que toma la `matriz` como parámetro.

    ```python
    def verificar_collisiones(matriz):
    ```

- Ahora todo lo que necesitas hacer es verificar si las posiciones `x, y` del astronauta corresponden a un elemento `ROJO` en la matriz. Si lo hace, puedes devolver `True`, y si no, devolver `False`.

--- hints ---
 --- hint ---
- La posición del astronauta está en `x` e `y`. Así que el elemento que necesitas estar chequeando está en `matriz[y][x]`.
--- /hint ---
 --- hint ---
- Dentro de tu función, utiliza una condición para verificar el elemento.
  ```python
  def verificar_collisiones(matriz):
      if matriz[y][x] == ROJO:
  ```
--- /hint --- --- hint ---
- Esta es la función completa:
  ```python
  def verificar_collisiones(matriz):
      if matriz[y][x] == ROJO:
          return True
      else:
          return False
  ```
--- /hint ------ /hints ---

- Ahora que estás verificando la colisión, puedes usar este condicional en tu ciclo de juego. Deberá estar tanto en el bucle "for" cómo en el bucle "while". Si este devuelve `True`, entonces puedes salir de los bucles.

```python
while True:
    matriz = gen_tuberias(matriz)
    if verificar_collisiones(matriz):
        break
    for i in range(3):
        matriz = mover_tuberias(matriz)
        sense.set_pixels(aplanar(matriz))
        sense.set_pixel(x, y, AMARILLO)   
        if verificar_collisiones(matriz):
            break
        sleep(1)
```
 <iframe src="https://trinket.io/embed/python/3b049d4b4a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>

