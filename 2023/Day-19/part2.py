from collections import deque

class PartRange:
    def __init__(self, bounds):
        # bounds = [lower_x, upper_x, lower_m, upper_m, lower_a, upper_a, lower_s, upper_s]
        self.bounds = bounds

    def value(self):
        total = 1
        for i in range(0, 8, 2):
            total *= self.bounds[i + 1] - self.bounds[i] + 1
        return total

    def split(self, attribute, comparaison, value):
        # Returns two PartRanges. The first is accepted and the second is refused.
        new_bounds = [self.bounds.copy() for _ in range(2)]
        index = 2 * "xmas".index(attribute)

        if comparaison:
            new_bounds[0][index] = value + 1
            new_bounds[1][index + 1] = value
        else:
            new_bounds[0][index + 1] = value - 1
            new_bounds[1][index] = value

        return tuple(PartRange(b) for b in new_bounds)

class Workflow:
    def __init__(self, instruction):
        instruction = instruction.split("{")
        self.rules, self.final = self.make_rules(instruction[1][:-1])

    def make_rules(self, rules_string):
        def parse_rule(rule):
            split = rule.split(":") 
            return (rule[0], rule[1] == ">", int(split[0][2:]), split[1])

        rules_string = rules_string.split(',')
        return list(map(parse_rule, rules_string[:-1])), rules_string[-1]
    
    def analyse(self, part):
        findings = []
        # Takes a PartRange and returns a list of (str, PartRange)
        for attribute, comparaison, value, result in self.rules:
            matched, unmatched = part.split(attribute, comparaison, value)

            findings.append((result, matched))
            part = unmatched
        findings.append((self.final, unmatched))
        
        return findings

workflows = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            break
        workflows[line.split("{")[0]] = Workflow(line.strip())

total = 0
q = deque([("in", PartRange([1, 4000, 1, 4000, 1, 4000, 1, 4000]))])
while q:
    workflow_name, part_range = q.popleft()
    findings = workflows[workflow_name].analyse(part_range)
    for workflow_name, part_range in findings:
        if workflow_name == "R":
            continue
        elif workflow_name == "A":
            total += part_range.value()
        else:
            q.append((workflow_name, part_range))
print(total)