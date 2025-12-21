import operator
import re

class Workflow:
    def __init__(self, instruction):
        instruction = instruction.split("{")
        self.rules, self.final = self.make_rules(instruction[1][:-1])

    def make_rules(self, rules_string):
        def parse_rule(rule):
            split = rule.split(":")
            return (rule[0], operator.gt if rule[1] == ">" else operator.lt, int(split[0][2:]), split[1])

        rules_string = rules_string.split(',')
        return list(map(parse_rule, rules_string[:-1])), rules_string[-1]
    
    def analyse(self, part):
        for category, comparaison, value, result in self.rules:
            if comparaison(getattr(part, category), value):
                return result.strip()
        return self.final.strip()
    
class Part:
    def __init__(self, s):
        self.x, self.m, self.a, self.s = map(int, re.findall(r"\d+", s))
    
    def value(self):
        return self.x + self.m + self.a + self.s

workflows = {}
parts = []
parsing_workflows = True
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            parsing_workflows = False
        elif parsing_workflows:
            workflows[line.split("{")[0]] = Workflow(line.strip())
        else:
            parts.append(Part(line.strip()))

total = 0
for part in parts:
    current = "in"
    while True:
        current = workflows[current].analyse(part)
        if current == "R":
            break
        elif current == "A":
            total += part.value()
            break
print(total)