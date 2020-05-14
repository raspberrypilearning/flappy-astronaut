import os
from glob import glob
import re

stappen = {}
files = [y for x in os.walk("./") for y in glob(os.path.join(x[0], '*.md'))]

for filename in files:
    with open(filename, 'r') as f:
        steps[int(re.findall(r'\d+', filename)[0])] = re.findall(r'##(.*)', f.read())
print("")
print("- title: Introduction")
print("- title: What you will need")
for i in range(3,len(steps)+1):
    print("- title:" + steps[i][0])
