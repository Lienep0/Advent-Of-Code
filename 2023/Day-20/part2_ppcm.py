from collections import deque
from math import lcm

class Module():
    def __init__(self, name, s, network):
        self.name = name
        self.neighbors = s.strip().split(" -> ")[1].split(", ")
        self.network = network

    def send_signal(self, pulse):
        for target_name in self.neighbors:
            self.network.pulse_queue.append((self.name, target_name, pulse))

class Broadcaster(Module):
    def __init__(self, name, s, network):
        super().__init__(name, s, network)

    def recieve_signal(self, _, pulse):
        self.send_signal(pulse)

class FlipFlop(Module):
    def __init__(self, name, s, network):
        super().__init__(name, s, network)
        self.state = False

    def recieve_signal(self, _, pulse):
        if not pulse:
            self.state = not self.state
            self.send_signal(self.state)

class Conjunction(Module):
    def __init__(self, name, s, network):
        super().__init__(name, s, network)
        self.connected_states = {}

    def add_connected(self, m):
        self.connected_states[m] = False

    def recieve_signal(self, name, pulse):
        self.connected_states[name] = pulse
        self.send_signal(not all(self.connected_states.values()))

class Network():
    def __init__(self):
        self.network = {}
        self.conjunction_modules = {}
        self.flipflop_modules = []
        self.total_pulses = {False: 0, True: 0}
        self.pulse_queue = deque()

        # Found with visualization.py
        self.important = ["ts", "xd", "vr", "pf"]

    def press_button(self):
        returnvalue = False, ""

        self.total_pulses[False] += 1
        self.network["broadcaster"].send_signal(False)
        while self.pulse_queue:
            sender, target_name, pulse = self.pulse_queue.popleft()
            target = self.network.get(target_name)

            if sender in self.important and not pulse:
                returnvalue = True, sender
            
            self.total_pulses[pulse] += 1
            if target != None:
                target.recieve_signal(sender, pulse)

        return returnvalue
    
    def press_until_rx(self):
        cycle_lengths = []

        i = 1
        while True:
            has_happened, important_module = self.press_button()
            if has_happened:
                print(f"{important_module} was pressed at button press number {i}")
                cycle_lengths.append(i)

                if len(cycle_lengths) == len(self.important):
                    print(lcm(*cycle_lengths))
                    exit()
            i += 1
        

network = Network()

# Set up general network
with open("input.txt", "r") as f:
    for line in f.readlines():
        module_type = Conjunction if line[0] == "&" else FlipFlop if line[0] == "%" else Broadcaster
        start = 0 if module_type == Broadcaster else 1
        name = line.strip()[start:].split(" -> ")[0]

        module = module_type(name, line, network)
        network.network[name] = module
        if module_type == Conjunction:
            network.conjunction_modules[name] = module
        elif module_type == FlipFlop:
            network.flipflop_modules.append(module)

# Set up Conjunction modules:
for m in network.network.values():
    for c in network.conjunction_modules:
        if c in m.neighbors:
            network.conjunction_modules[c].add_connected(m.name)

print(network.press_until_rx())