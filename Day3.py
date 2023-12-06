import numpy as np
import regex as re


input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

#inputLines = input.splitlines()

#lenOfLines = len(inputLines[0])

#lineArray = np.asarray(inputLines).reshape((lenOfLines,-1))

xout = [ x for x in input]

arrayY = np.asarray(xout)
arrayY = arrayY[arrayY != '\n']
arrayY = arrayY.reshape(input.find('\n'),-1)

arrayY = np.char.replace(arrayY, '.','')

numbers = re.findall(r'\d*',input)
