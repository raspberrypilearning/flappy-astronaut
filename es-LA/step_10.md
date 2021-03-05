## Moviendo las tuberías

Como se menciona en la sección anterior, el algoritmo para mover las tuberías tendrá que repetirse cada vez que quieras desplazar los píxeles a la izquierda por `1`. Cualquier código que necesite ser repetido puede ser colocado dentro de una función. Crea esta función debajo de tu función `gen_tuberias(matriz)`:

```python
def mover_tuberias(matriz):
```
El algoritmo para esta función puede ser desglosado así:
  1. Por cada fila de la matriz
     1. Por cada elemento en la fila de `0` a `7`
     1. Configura el elemento para que sea el mismo que el siguiente elemento en la fila
  1. Establece el último elemento de la fila para ser `AZUL`.

- Intenta y completa esto por ti mismo, y utiliza las siguientes sugerencias si necesitas ayuda.

--- hints ---
 --- hint ---
- Dentro de la función puedes comenzar tu ciclo de esta manera:
```python
def mover_tuberias(matriz):
    for fila in matriz:
        for i in range(7):
```
--- /hint --- --- hint ---
- Para cambiar los elementos, puedes usar su índice.
```python
def mover_tuberias(matriz):
    for fila in matriz:
        for i in range(7):
            fila[i] = fila[i + 1]
```
--- /hint --- --- hint ---
- Para terminar, configura el último elemento de cada fila para que sea `AZUL`, y luego regresa la matriz alterada.
```python
def mover_tuberias(matriz):
    for fila in matriz:
        for i in range(7):
            fila[i] = fila[i + 1]
        fila[-1] = AZUL
    return matriz
```
--- /hint ------ /hints ---
