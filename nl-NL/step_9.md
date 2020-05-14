## Bewegend buizen-algoritme

Nu je zoveel buizen kunt genereren als je wilt, moet je ze over de matrix verplaatsen zodat ze naar de linkerkant van het scherm gaan.

Het is misschien gemakkelijker om dit op een kleinere schaal te bekijken. Hier is bijvoorbeeld een 5 × 5-matrix:

```
  0 1 2 3 4
0 b b b b r
1 b b b b r
2 b b b b b
3 b b b b r
4 b b b b r
```
Om de rode pixels (`r`) naar links te verplaatsen, kun je een eenvoudig algoritme volgen:
  1. Verplaats alle items op index `1` in elk van de rijen naar index `0`
  1. Verplaats alle items op index `2` in elk van de rijen naar index `1`
  1. Verplaats alle items op index `3` in elk van de rijen naar index `2`
  1. Verplaats alle items op index `4` in elk van de rijen naar index `3`
  1. Vul alle items op index `5` in elke rij met een `b`

Dit zou je dan een matrix geven die er zo uitziet:

```
  0 1 2 3 4
0 b b b r b
1 b b b r b
2 b b b b b
3 b b b r b
4 b b b r b
```
Je zou het algoritme opnieuw kunnen uitvoeren om de beweging te herhalen, wat je dit zou geven:

```
  0 1 2 3 4
0 b b r b b
1 b b r b b
2 b b b b b
3 b b r b b
4 b b r b b
```
Als je dit met jouw matrix doet, gebeurt het volgende:

![buizen verplaatsen](images/SH-1.gif)
