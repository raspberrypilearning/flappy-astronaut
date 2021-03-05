import os
from glob import glob
import re

pasos = {}
archivos = [y for x in os.walk(“./“) for y in glob(os.path.join(x[0], ‘*.md’))]

for nombres in archivos:
    with open(nombres, ‘r’) as a:
        pasos[int(re.findall(r'\d+', nombres)[0])] = re.findall(r'##(.*)', a.read())
print("")
print("- título: Introducción")
print("- título: Lo que vas a necesitar")
for i in range(3,len(pasos)+1):
    print("- título:" + pasos[i][0])
