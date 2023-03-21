import random

class Circuit:
    def __init__(self, voltage, resistance):
        self.voltage = voltage
        self.resistance = resistance
        self.current = voltage / resistance

    def update_current(self):
        self.current = self.voltage / self.resistance

    def update_voltage(self):
        self.voltage = self.current * self.resistance

    def update_resistance(self):
        self.resistance = self.voltage / self.current

circuits = [Circuit(random.uniform(0, 100), random.uniform(0, 100)) for i in range(10)]
for c in circuits:
    print("Voltage:", c.voltage, "Resistance:", c.resistance, "Current:", c.current)