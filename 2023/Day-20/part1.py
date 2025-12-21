from collections import deque

class Module():
    def __init__(self, name, s, network):
        self.name = name
        self.neighbors = s.strip().split(" -> ")[1].split(", ")
        self.network = network

    def send_signal(self, pulse):
        for n in self.neighbors:
            target = self.network.network.get(n)
            self.network.pulse_queue.append((self.name, target, pulse))

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

    def press_button(self):
        self.total_pulses[False] += 1
        self.network["broadcaster"].send_signal(False)
        while self.pulse_queue:
            sender, target, pulse = self.pulse_queue.popleft()
            # print(f"{sender} sent a {pulse} pulse to {target.name if target != None else "output"}")
            self.total_pulses[pulse] += 1
            if target != None:
                target.recieve_signal(sender, pulse)

    def hash(self):
        return int(''.join(["1" if m.state else "0" for m in self.flipflop_modules]), 2)
    
    def find_total_pulses(self, n=1000):
        button_presses = 1
        self.press_button()
        while self.hash() > 0:
            if button_presses == n:
                return self.total_pulses[False] * self.total_pulses[True]
            button_presses += 1
            self.press_button()

        print(f"Found a cycle after {button_presses} button presses")
        return self.total_pulses[False] * self.total_pulses[True] * ((n // button_presses) ** 2)

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

print(network.find_total_pulses())