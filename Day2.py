import pyperclip as pc
import regex as re
import numpy as np

input = re.split(r'\n?Game \d\d?\d?: ',pc.paste())

input = input[1:]

maxDict = {'red' : 12,
           'green' : 13,
           'blue': 14}

indexes = [item for item in range(1,len(input)+1)]
indexesFailed = []
powers = []

for line in range(len(input)):
    sectioned = re.split(r'\W? ', input[line])
    length = len(sectioned)
    dictRound = {'red' : 0,
           'green' : 0,
           'blue': 0}
    for i in range(0,length,2):
        if int(sectioned[i]) > dictRound[sectioned[i + 1]]:
            dictRound[sectioned[i+1]] = int(sectioned[i])
        if int(maxDict[sectioned[i+1]]) < int(sectioned[i]):
            if int(line) + 1 not in indexesFailed:
                indexesFailed.append(int(line) + 1)
    subPowers = list(dictRound.values())
    powers.append(np.prod(subPowers))
        
print(sum(powers))          
successes = [x for x in indexes if x not in indexesFailed]
print(sum(successes))
    