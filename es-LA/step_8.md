## Crea una función para hacer más tuberías

El juego sería un poco fácil si solo fuesen creadas un conjunto de tuberías. Puedes generar tantas tuberías como desees usando una función.

- Debajo de tu función `aplanar()`, crea una nueva función llamada `gen_tuberias`:

    ```python
    def gen_tuberias(matriz):
    ```

- Pon el código que escribiste para generar un conjunto de tuberías en esta función. Simplemente puedes agregar algo de sangría para hacer esto. Al final de la función, deberías `retornar` la `matriz` alterada.
  ```python
  def gen_tuberias(matriz):
      for fila in matriz:
        fila[-1] = ROJO
      abertura = randint(1, 6)
      matriz[abertura][-1] = AZUL
      matriz[abertura - 1][-1] = AZUL
      matriz[abertura + 1][-1] = AZUL
      return matriz
  ```

- Luego, llama a la función antes de aplanar y mostrar la `matriz`.

    ```python
    matriz = gen_tuberias(matriz)
matriz = aplanar(matriz)
sensor.set_pixels(matriz)
    ```

- Así es como debería verse tu código ahora: 
<iframe src="https://trinket.io/embed/python/04a85934e4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>


