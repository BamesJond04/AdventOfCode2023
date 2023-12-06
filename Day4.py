import pyperclip as pc
import regex as re

input = pc.paste().splitlines()

p= re.compile(r'Card \d+: ')
wS = re.compile(r' +')

sectioned = [(p.sub('',line)).split('|') for line in input]


scores = []

#for x in range(len(sectioned)):
 #   i = sectioned[x]
  #  correctNumbers = wS.split((i[0].strip()))
   # yourNumbers = wS.split((i[1].strip()))
    #count = 0
#    for number in correctNumbers:
 #       if number in yourNumbers:
  #          count += 1
   # for i in reversed(range(1,count+1)):
#        print(i)
 #       sectioned = sectioned[:x+i] + [sectioned[x+i]] + sectioned[x+i:]
  #      cardCount[x+i] += 1
   # if count >= 1: scores.append(2**(count-1))
    #if count == 0: scores.append(0)


for index, item in enumerate(sectioned):
    correctNumbers = wS.split((item[0].strip()))
    yourNumbers = wS.split((item[1].strip()))
    count = 0
    for number in correctNumbers:
        if number in yourNumbers:
            count += 1
    for  i in reversed(range(1,count+1)):
        last = sectioned[::-1].index(item)
        sectioned = sectioned[:last+1:-1] + sectioned[-last] 
    if count >= 1: scores.append(2**(count-1))
    if count == 0: scores.append(0)

print(sum(scores))
