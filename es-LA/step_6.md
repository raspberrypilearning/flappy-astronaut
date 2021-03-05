## Generando tuberías

En Astronauta Aleteador, el astronauta deberá evitar las 'tuberías' que brotan de la parte superior e inferior de la matriz. El color de las tuberías va a ser rojo.

Para empezar, puedes crear una sola columna de píxeles rojos en el lado derecho de la matriz.

![columnas](images/SH-1.png)

Todo lo que necesitas hacer es configurar el último elemento en cada una de las listas dentro de la matriz para que sea `ROJO` en lugar de `AZUL`. A continuación hay un repaso de cómo acceder a los elementos en una lista.

[[[generic-python-list-index]]]

- Puedes usar un bucle para que, por cada lista en la matriz, el último elemento sea configurado a `ROJO`. Coloca este bucle for loop de modo que este se ejecute antes de aplanar y mostrar la matriz. Puedes utilizar los consejos a continuación para ayudarte si es que los necesitas.

--- hints ---
 --- hint ---
- Aquí hay un ejemplo de cómo debería verse tu código, con algunos comentarios agregados sobre dónde debe ir tu bucle.
    ```python
    from sense_hat import SenseHat

    sense = SenseHat()
    ROJO = (255, 0, 0)
    AZUL = (0, 0, 255)

    matriz = [[AZUL for columna in range(8)] for fila in range(8)]

    def aplanar(matriz):
      aplanada = [pixel for fila in matriz for pixel in fila]
      return aplanada


    ## Coloca tu bucle aquí

    matriz = aplanar(matriz)
    sense.set_pixels(matriz)
    ```
--- /hint --- --- hint ---
- Tu bucle for debe repetirse sobre las listas dentro de la matriz.
    ```python
    for fila in matriz:
    ```
--- /hint --- --- hint ---
- Luego, asigna el último elemento de cada lista a `ROJO`.
    ```python
    for fila in matriz:
        fila[-1] = ROJO
    ```
- Esto es lo que debería hacer: 
<iframe src="https://trinket.io/embed/python/f553d03f1b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>
--- /hint ---
--- /hints ---
