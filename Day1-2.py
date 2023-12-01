import pyperclip as pc

input = (pc.paste())
input = input.splitlines()

countsAs = ['one','two','three','four','five','six','seven','eight','nine']
numbers= ['1','2','3','4','5','6','7','8','9']

input2 = []

for line in input:
    first = ''
    while first != 'finished':
        first = next((s for s in countsAs if s in line), 'finished')
        if first != 'finished':
            replacer = (countsAs[countsAs.index(first)])[0]+ numbers[countsAs.index(first)] + (countsAs[countsAs.index(first)])[-1]
            line = line.replace(first,replacer)
    input2.append(line)
outNum = []        
for i in input2:
    short = [int(x) for x in i if x.isdigit()]
    lineNumber = str(short[0]),str(short[-1])
    output= ''.join(lineNumber)
    outNum.append(int(output))
    
print(sum(outNum))
