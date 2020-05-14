## De buizen verplaatsen

Zoals eerder vermeld in het gedeelte, moet het algoritme om de pijpen te verplaatsen telkens worden herhaald als je de pixels met `1` naar links wilt verschuiven. Elke code die moet worden herhaald, kan in een functie worden geplaatst. Maak deze functie onder je `gen_pipes(matrix)` functie:

```python
def beweeg_buizen(matrix):
```
Het algoritme voor deze functie kan als volgt worden opgesplitst:
  1. Voor elke rij in de matrix
     1. Voor elk item in de rij van `0` tot `7`
     1. Stel het item hetzelfde in als het volgende item in de rij
  1. Stel het laatste item in de rij in op `BLAUW`.

- Probeer dit zelf uit te voeren en gebruik de onderstaande tips als je hulp nodig hebt.

--- hints --- --- hint ---
- Binnen de functie kun je je for loop als volgt beginnen:
```python
def beweeg_buizen(matrix):
    for row in matrix:
        for i in range(7):
```
--- /hint ---
--- hint ---
- Om de items om te schakelen, kun je hun index gebruiken.
```python
def beweeg_buizen(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
```
--- /hint ---
--- hint ---
- Stel om te eindigen het laatste item in elke rij in op `BLAUW`en retourneer vervolgens de gewijzigde matrix.
```python
def beweeg_buizen(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
        row[-1] = BLAUW
    return matrix
```
--- /hint --- 
--- /hints ---
