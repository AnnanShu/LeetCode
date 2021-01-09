class Automaton:
    def __init__(self):
        self.state = 'start'
        self.numbered = False
        self.table = {
            'start': ['start', 'insign', 'dot', 'innumber', 'end', 'end'],
            'insign':['end', 'end', 'dot', 'innumber', 'end', 'end'],
            'innumber':['endspace', 'end', 'dot', 'innumber', 'e', 'end'],
            'dot':['endspace', 'end', 'end', 'dotted', 'end', 'end'],
            'dotted':['endspace', 'end', 'end', 'dotted', 'e', 'end'],
            'e':['end', 'outsign', 'end', 'outnumber', 'end', 'end'],
            'outsign':['end', 'end', 'end', 'outnumber', 'end', 'end'],
            'outnumber':['endspace', 'end', 'end', 'outnumber', 'end', 'end'],
            'endspace':['endspace', 'end', 'end', 'end', 'end', 'end'],
            'end': ['end', 'end', 'end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        if c.isspace(): return 0
        if c == '+' or c == '-': return 1
        if c == '.': return 2
        if c.isdigit(): return 3
        if c == 'e': return 4
        return 5
    
    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)] 
        if self.state in ['innumber', 'dotted', 'outnumber']:
            self.numbered = True
class Solution:
    def isNumber(self, s: str) -> bool:
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        print(automaton.state, automaton.numbered)
        return automaton.state != 'start' and automaton.state != 'end' and automaton.state != 'e' and automaton.numbered