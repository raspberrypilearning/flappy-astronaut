## Mirando el movimiento de las tuberías

Por el momento, ejecutar tu código no hará mucho. Necesitas llamar a tus funciones en un bucle para verlo funcionar.

En este momento deberías tener estas tres líneas en la parte inferior de tu código:

```python
matriz = gen_tuberias(matriz)
matriz = aplanar(matriz)
sensor.set_pixels(matriz)
```

- En lugar de utilizar dos líneas de código para aplanar la matriz y luego mostrarla, puede utilizar una sola línea para hacer esto. Esto evitará el aplanamiento de la matriz original cada vez, y en su lugar simplemente usar una versión aplanada de la matriz para la pantalla. Reemplaza las tres últimas líneas con esto:

```python
matriz = gen_tuberias(matriz)
sensor.set_pixels(aplanar(matriz))
```

- Ahora puedes añadir tu función `mover_tuberias(matriz)` para mover las tuberías:

```python
matriz = gen_tuberias(matriz)
sensor.set_pixels(aplanar(matriz))
matriz = mover_tuberias(matriz)
```
- Aunque esto moverá las tuberías, estas no se mostrarán, ya que no hay una segunda llamada a `set_pixels`. Para resolver esto, puedes añadir un ciclo para que moviendo y mostrando siempre sigan en sequencia.

```python
matriz = gen_tuberias(matriz)
for i in range(9):
    sensor.set_pixels(aplanar(matriz))
    matriz = mover_tuberias(matriz)
```

Prueba y ejecuta este código, y mira qué sucede. ¿Fue un poco rápido?

- Puedes resolver esto añadiendo un comando `sleep()`. En la parte superior de tu código, importa el método `sleep` del módulo `time`:

```python
from time import sleep
```

- Luego añade un comando `sleep` en tu bucle:

```python
matriz = gen_tuberias(matriz)
for i in range(9):
    sensor.set_pixels(aplanar(matriz))
    matriz = mover_tuberias(matriz)
    sleep(1)
```

- Si ejecutas el código ahora, deberías ver algo un poco más parecido a esto: 
<iframe src="https://trinket.io/embed/python/74307750be" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>

- Una pequeña alteración te dará un flujo continuo de tuberías. Simplemente cambia el bucle for para repetir `3` o `4` veces, y luego adjunta toda la última sección del código en un bucle infinito `while True`:

```python
while True:
  matriz = gen_tuberias(matriz)
  for i in range(3):
      sensor.set_pixels(aplanar(matriz))
      matriz = mover_tuberias(matriz)
      sleep(1)
```

- Esto debería darte algo que se vea así: 
<iframe src="https://trinket.io/embed/python/46cf11b0c9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>
