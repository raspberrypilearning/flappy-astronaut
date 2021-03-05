## Utilizando listas 2D con el Sense HAT

Ahora que sabes que la mejor manera de representar los píxeles en la matriz LED es usando una lista 2D, veamos cómo se puede hacer esto con el Sense HAT.

- Abre un nuevo archivo Python, o utiliza el emulador Sense HAT en [trinket.io](https://trinket.io/).

- Con las dos primeras líneas de código, importa los módulos Sense HAT y crea un objeto `SenseHAT` que puede ser utilizado para controlar la matriz LED:

```python
from sense_hat import SenseHat

sensor = SenseHat()
```

Luego, necesitas crear dos variables que representen los colores de los píxeles. Para hacer esto sencillo, puedes usar rojo y azul. Si deseas aprender un poco más sobre cómo las computadoras representan los colores, observa la sección a continuación.

[[[generic-theory-colours]]]

- Para almacenar la información del color, puedes utilizar un par de tuplas o secuencias invariables, una para rojo y otra para azul.

```python
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
```

- Ahora vas a crear una lista de listas llenas con la variable `AZUL`. Crearlo manualmente significaría escribir mucho, pero en su lugar puedes usar una comprensión de lista para completar la tarea en una sola línea.

```python
matriz = [[AZUL for columna in range(8)] for fila in range(8)]
```

¿Qué hace este código? La sección `[AZUL for columna in range(8)]` crea una lista con ocho valores de `(0, 0, 255)` dentro de ella. Luego, la parte `for fila in range(8)` hace ocho copias de esa lista dentro de otra lista. Después de ejecutar el código, puedes cambiar al intérprete y escribir `matriz` si deseas ver el resultado por tí mismo.

Si deseas obtener más información sobre las comprensiones de listas, echa un vistazo a la sección a continuación.

[[[generic-python-simple-list-comprehensions]]]

No puedes utilizar esta lista de listas con el Sense HAT, ya que tu software sólo entiende una lista **plana** de una sola dimensión. Para solucionar este problema, vas a crear una función que convierte las listas 2D en listas 1D. Entonces, puedes usar esta función cada vez que la `matriz` necesite ser mostrada.

Para aplanar una lista 2D en una lista 1D, puedes usar nuevamente una comprensión de lista. Aquí hay un ejemplo de cómo aplanar una lista.

```python
aplanada = [pixel for fila in matriz for pixel in fila]
```

¿Qué hace esto? La parte `for fila in matriz` mira a cada una de las listas de la matriz, y la sección `for pixel in fila` mira a los píxeles individuales en cada fila de esa lista. Entonces, estos píxeles son colocados todos en una sola lista.

- Puedes convertir esto en una función para evitar tener que escribirlo todo el tiempo. Agrega esto a tu archivo:

```python
def aplanar(matriz):
    aplanada = [pixel for fila in matriz for pixel in fila]
    return aplanada
```

- Para aplanar tu matriz y luego mostrarla en el Sense HAT, ahora puedes simplemente añadir estas líneas de código a la parte inferior de tu archivo.

```python
matriz = aplanar(matriz)
sensor.set_pixels(matriz)
```
- Graba y ejecuta tu código. Puedes ver un ejemplo del código y de su salida en el trinket incrustado a continuación. 
<iframe src="https://trinket.io/embed/python/b4c1aad6c3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe>
