from typing import Optional
import math

class Module():
    def __init__(self, name: str):
        self.name = name
    
    def read(self):
        return 0
    
    def __repr__(self):
        return "Module " + self.name


class FlipFlop():
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.state = 0
        self.outputs = outputs
    
    def flip(self):
        self.state = 1 - self.state
    
    def read(self) -> int:
        return self.state
    
    def get_output_signal(self, input_signal: int) -> Optional[int]:
        if input_signal == 0:
            self.flip()
            return self.state
    
    def __repr__(self):
        return "FlipFlop " + self.name + ": " + str(self.state) + " sending to " + str(self.outputs)


class Conjunction():
    def __init__(self, name: str, input_sources: list[str], outputs: list[str]):
        self.name = name
        self.inputs = {source: 0 for source in input_sources}
        self.outputs = outputs
    
    def read(self) -> tuple[int]:
        return tuple(self.inputs.values())

    def add_input_source(self, source: str):
        self.inputs[source] = 0

    def update_input(self, source: str, signal: int):
        self.inputs[source] = signal
    
    def get_output_signal(self) -> int:
        if all(self.inputs.values()):
            return 0
        return 1
    
    def __repr__(self):
        return "Conjunction " + self.name + ": " + str(self.inputs) + " sending to " + str(self.outputs)


class Broadcaster():
    def __init__(self, outputs: list[str]):
        self.outputs = outputs
    
    def read(self) -> int:
        return 0

    def __repr__(self):
        return "Broadcaster: " + str(self.outputs)


def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    modules = {}
    for line in out:
        component, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if component == 'broadcaster':
            modules[component] = Broadcaster(outputs)
        elif component[0] == '%':
            modules[component[1:]] = FlipFlop(component[1:], outputs)
        elif component[0] == '&':
            modules[component[1:]] = Conjunction(component[1:], [], outputs)
        else:
            modules[component] = Module(component)
    for line in out:
        component, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        for output in outputs:
            if output not in modules:
                modules[output] = Module(output)
            out_component = modules[output]
            if type(out_component) == Conjunction:
                out_component.add_input_source(component[1:])

    # print(modules)
    total_low_pulses = 0
    total_high_pulses = 0
    states = {}
    count = 0
    # for component in modules:
    #     print(component, modules[component].read())
    # print()
    N = 1000
    while count < N:
        prior_state = tuple(modules[component].read() for component in modules)
        if prior_state in states:
            break
        else:
            # print("Pressing button now")
            count += 1
            num_low_pulses = 0
            num_high_pulses = 0
            signal_queue = [('button', 0)]
            while signal_queue:
                source, signal = signal_queue.pop(0)
                # print(source, signal)
                if source == 'button':
                    num_low_pulses += 1
                    output = 'broadcaster'
                    signal_queue.append((output, signal))
                    continue
                component = modules[source]
                # print(component)
                if type(component) == Broadcaster:
                    for output in component.outputs:
                        signal_queue.append((output, signal))
                        out_component = modules[output]
                        if type(out_component) == Conjunction:
                            out_component.update_input(source, signal)
                    if signal == 0:
                        num_low_pulses += len(component.outputs)
                    elif signal == 1:
                        num_high_pulses += len(component.outputs)
                    
                elif type(component) == FlipFlop:
                    output_signal = component.get_output_signal(signal)
                    # print("Output signal:", output_signal)
                    if output_signal is not None:
                        for output in component.outputs:
                            signal_queue.append((output, output_signal))
                            out_component = modules[output]
                            if type(out_component) == Conjunction:
                                out_component.update_input(source, output_signal)
                        if output_signal == 0:
                            num_low_pulses += len(component.outputs)
                        elif output_signal == 1:
                            num_high_pulses += len(component.outputs)
                    
                elif type(component) == Conjunction:
                    output_signal = component.get_output_signal()
                    # print("Output signal:", output_signal)
                    for output in component.outputs:
                        signal_queue.append((output, output_signal))
                        out_component = modules[output]
                        if type(out_component) == Conjunction:
                            out_component.update_input(source, output_signal)
                    if output_signal == 0:
                        num_low_pulses += len(component.outputs)
                    else:
                        num_high_pulses += len(component.outputs)
                
            states[prior_state] = (num_low_pulses, num_high_pulses)
            total_low_pulses += num_low_pulses
            total_high_pulses += num_high_pulses
    
    if count < N:
        # print("Cycle detected")
        # print(states)
        unwrapped_states = list(states.keys())
        curr_ind = unwrapped_states.index(prior_state)
        while count < N:
            # print(prior_state)
            total_low_pulses += states[prior_state][0]
            total_high_pulses += states[prior_state][1]
            count += 1
            curr_ind = (curr_ind + 1) % len(unwrapped_states)
            prior_state = unwrapped_states[curr_ind]
    print(total_low_pulses)
    print(total_high_pulses)
    print(total_high_pulses * total_low_pulses)


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    
    modules = {}
    for line in out:
        component, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if component == 'broadcaster':
            modules[component] = Broadcaster(outputs)
        elif component[0] == '%':
            modules[component[1:]] = FlipFlop(component[1:], outputs)
        elif component[0] == '&':
            modules[component[1:]] = Conjunction(component[1:], [], outputs)
        else:
            modules[component] = Module(component)
    for line in out:
        component, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        for output in outputs:
            if output not in modules:
                modules[output] = Module(output)
            out_component = modules[output]
            if type(out_component) == Conjunction:
                out_component.add_input_source(component[1:])

    end_flag = True
    num_button_presses = 0
    useful_modules = ['sb', 'nd', 'ds', 'hf']
    while not end_flag:
        num_button_presses += 1
        signal_queue = [('button', 0)]
        while signal_queue:
            source, signal = signal_queue.pop(0)
            if source == 'button':
                output = 'broadcaster'
                signal_queue.append((output, signal))
                continue

            component = modules[source]

            if type(component) == Broadcaster:
                for output in component.outputs:
                    signal_queue.append((output, signal))
                    if output == 'rx' and signal == 0:
                        end_flag = True
                        break
                    elif output in useful_modules and output_signal == 0:
                        print(num_button_presses, output)
                    out_component = modules[output]
                    if type(out_component) == Conjunction:
                        out_component.update_input(source, signal)
                
            elif type(component) == FlipFlop:
                output_signal = component.get_output_signal(signal)
                if output_signal is not None:
                    for output in component.outputs:
                        signal_queue.append((output, output_signal))
                        if output == 'rx' and output_signal == 0:
                            end_flag = True
                            break
                        elif output in useful_modules and output_signal == 0:
                            print(num_button_presses, output)
                        out_component = modules[output]
                        if type(out_component) == Conjunction:
                            out_component.update_input(source, output_signal)
                
            elif type(component) == Conjunction:
                output_signal = component.get_output_signal()
                for output in component.outputs:
                    signal_queue.append((output, output_signal))
                    if output == 'rx' and output_signal == 0:
                        end_flag = True
                        break
                    elif output in useful_modules and output_signal == 0:
                        print(num_button_presses, output)
                    out_component = modules[output]
                    if type(out_component) == Conjunction:
                        out_component.update_input(source, output_signal)

    periods = {'vv': 3797, 
               'nt': 3917,
               'vn': 3733,
               'zq': 3877}
    
    # compute lcm of periods
    lcm = periods['vv']
    for key in periods:
        lcm = lcm * periods[key] // math.gcd(lcm, periods[key])

    print(lcm)
    

part1()
part2()