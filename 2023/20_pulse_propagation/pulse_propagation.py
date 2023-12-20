''' Advent of Code 2023
    Day 20: Pulse Propagation
    https://adventofcode.com/2023/day/20

Status:
    - Part 1:
        * Test 1: TBD
        * Puzzle: TBD
    - Part 2:
        * Test 2: TBD
        * Puzzle: TBD
'''

import queue
import re

from itertools import pairwise

# 0. Functions that are common to both problems

class Module(object):
    def __init__(self, name:str, destination:list, state:bool=False):
        self.name = name
        self.destination = destination
        self.state = state
        self.pulse = False
        print(self.name, self.destination, self.state, self.pulse)

    def process_pulse(self, pulse:bool, *args):
        self.pulse = pulse
        self.send_pulses()

    def send_pulses(self):
        print(self.destination)
        for receiver_name in self.destination:
            print(receiver_name)
            PulsePropagator.queue.put((self.name, self.pulse, receiver_name)) 

class Broadcaster(Module):
    pass

class FlipFlop(Module):
    def process_pulse(self, pulse:bool, *args):
        if (pulse):
            # high pulse --> ignore
            return
        # otherwise, flip between on and off
        self.state = not self.state
        # If it was off, it switches on and sends a high pulse.
        # If it was on, it turns off and sends a low pulse.
        self.pulse = self.state

        self.send_pulses()

class Conjunction(Module):
    def add_connected_sender(self, sender_name:str):
        try:
            self.memory[sender_name] = False
        except:
            self.memory = {sender_name: False}

    def process_pulse(self, pulse:bool, sender_name:str, *args):
        # First it updates its memory for that input.
        self.memory[sender_name] = pulse

        # If it remembers high pulses (True) for all inputs (senders in memory),
        # it sends a low pulse (False); otherwise, it sends a high pulse (True).
        self.pulse = not(all(self.memory.values()))

        self.send_pulses()

class PulsePropagator(object):

    LINE_PATTERN = re.compile('([^\s]+) \-\> ([\w\,\s]+)')
    TYPES = {'b': Broadcaster, '%': FlipFlop, '&': Conjunction}

    queue = queue.SimpleQueue()

    def __init__(self, filepath:str):
        self.modules = {}
        with open(filepath, 'r') as f:
            while (input_line := f.readline().strip('\n\s\t')):
                self.process_input_line(input_line)

        print(self.modules)

        # Connect Conjunction inputs
        conjunctions = filter(lambda m: type(m) == 'Conjunction', self.modules)
        for conjunction in conjunctions:
            module_name = conjunction.name
            senders = filter(lambda m: module_name in m.destination, self.modules)
            for sender in senders:
                conjunction.add_connected_sender(sender.name)

        # Create the button
        button = Module('button', ['broadcaster',])
        button.send_pulses()

        while (pulse_tuple := self.queue.get()):
            print(pulse_tuple)
            sender_name, pulse, module_name = pulse_tuple
            print(sender_name, pulse, module_name)
            self.modules[module_name].process_pulse(pulse, sender_name)


    def process_input_line(self, input_line:str):
        parse_input = self.LINE_PATTERN.search(input_line)
        module_name = parse_input.group(1)
        module_type = module_name[0]
        if (module_type != 'b'):
            module_name = module_name[1:]
        destination = parse_input.group(2).split(", ")
        self.modules[module_name] = self.TYPES[module_type](module_name, destination)

# 1. Functions that are specific for problem 1

def solve_part_1(filepath:str, with_hex:bool=False):
    pulse_propagator = PulsePropagator(filepath)
    return 1  # TODO: map correct output

# 2. Functions that are specific for problem 2

def solve_part_2(filepath:str, with_hex:bool=False):
    pulse_propagator = PulsePropagator(filepath)
    return 1  # TODO: map correct output

if __name__ == '__main__':
    # assert(solve_part_1('test_01.txt') == 62)
    # assert(pipe_maze_1('puzzle_input.txt') == 6733)

    print(solve_part_1('test_01.txt'))
