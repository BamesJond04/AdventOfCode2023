import pyperclip as pc

input = (pc.paste())
numbers = []

inputRep = input.splitlines()


for i in inputRep:
    short = [int(x) for x in i if x.isdigit()]
    lineNumber = str(short[0]),str(short[-1])
    output= ''.join(lineNumber)
    numbers.append(int(output))
    
print(sum(numbers))
#