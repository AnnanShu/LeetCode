from functools import reduce
import sys, operator
def mul(s):
    return reduce(operator.mul, [int(num) for num in s.split('*')])
line = sys.stdin.readline()

while line != 'END\n':
    new_str = line.replace('-', '+-')
    print(sum([mul(each) if '*' in each else int(each) for each in new_str.split('+')]))
    line = sys.stdin.readline()


