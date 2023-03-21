# Import modules
import tkinter as tk
import math


# Define classes
class CircuitElement:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = None
        self.connectedTo = []

    def draw(self):
        pass

    def move(self, x, y):
        self.canvas.move(self.id, x, y)
        self.x = x
        self.y = y

    def connectTo(self, other):
        self.connectedTo.append(other)

    def disconnect(self, other):
        self.connectedTo.remove(other)


class Wire(CircuitElement):
    def draw(self):
        self.id = self.canvas.create_line(self.x, self.y, self.x + 10, self.y, fill="black")

    def move(self, x, y):
        super().move(x, y)
        coords = self.canvas.coords(self.id)
        self.canvas.coords(self.id, coords[0], coords[1],
                           coords[2] + x, coords[3] + y)


class Switch(CircuitElement):
    def __init__(self, canvas, x, y, state):
        super().__init__(canvas, x, y)
        self.state = state

    def draw(self):
        if self.state:
            fill = "green"
        else:
            fill = "red"
        self.id = self.canvas.create_oval(self.x, self.y,
                                          self.x + 10, self.y + 10,
                                          fill=fill)

    def switch(self):
        self.state = not self.state
        self.draw()


class LightBulb(CircuitElement):
    def __init__(self, canvas, x, y, state):
        super().__init__(canvas, x, y)
        self.state = state

    def draw(self):
        if self.state:
            fill = "yellow"
        else:
            fill = "grey"
        self.id = self.canvas.create_oval(self.x, self.y,
                                          self.x + 10, self.y + 10,
                                          fill=fill)

    def switch(self):
        self.state = not self.state
        self.draw()


class AutomaticSwitch(Switch):
    def __init__(self, canvas, x, y, state, time):
        super().__init__(canvas, x, y, state)
        self.time = time
        self.canvas.after(self.time, self.switch)

    def switch(self):
        super().switch()
        self.canvas.after(self.time, self.switch)


class Ammeter(CircuitElement):
    def __init__(self, canvas, x, y, voltage):
        super().__init__(canvas, x, y)
        self.voltage = voltage
        self.current = 0

    def draw(self):
        self.id = self.canvas.create_text(self.x, self.y,
                                          text=str(self.current))

    def calculateCurrent(self):
        self.current = self.voltage / len(self.connectedTo)

    def update(self):
        self.calculateCurrent()
        self.canvas.itemconfig(self.id, text=str(self.current))


class Voltmeter(CircuitElement):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)
        self.voltage = 0

    def draw(self):
        self.id = self.canvas.create_text(self.x, self.y,
                                          text=str(self.voltage))

    def calculateVoltage(self):
        self.voltage = 0
        for other in self.connectedTo:
            if isinstance(other, Ammeter):
                self.voltage += other.voltage

    def update(self):
        self.calculateVoltage()
        self.canvas.itemconfig(self.id, text=str(self.voltage))


class Wattmeter(CircuitElement):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)
        self.power = 0

    def draw(self):
        self.id = self.canvas.create_text(self.x, self.y,
                                          text=str(self.power))

    def calculatePower(self):
        self.power = 0
        for other in self.connectedTo:
            if isinstance(other, Ammeter):
                self.power += other.voltage * other.current

    def update(self):
        self.calculatePower()
        self.canvas.itemconfig(self.id, text=str(self.power))


class FrequencyMeter(CircuitElement):
    def __init__(self, canvas, x, y, frequency):
        super().__init__(canvas, x, y)
        self.frequency = frequency

    def draw(self):
        self.id = self.canvas.create_text(self.x, self.y,
                                          text=str(self.frequency))

    def update(self):
        self.canvas.itemconfig(self.id, text=str(self.frequency))


# Draw the circuit
def drawCircuit(circuit):
    canvas.delete("all")
    for el in circuit:
        el.draw()
    for el in circuit:
        for other in el.connectedTo:
            coords = canvas.coords(el.id)
            other_coords = canvas.coords(other.id)
            canvas.create_line(coords[0] + 5, coords[1] + 5,
                               other_coords[0] + 5, other_coords[1] + 5)


# Calculate the power
def calculatePower(circuit):
    power = 0
    for el in circuit:
        if isinstance(el, Wattmeter):
            el.update()
            power += el.power
    return power


# Define window
window = tk.Tk()
window.title("Circuit Simulator")
window.geometry("500x500")

# Define canvas
canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()

# Instantiate the elements
circuit = [Wire(canvas, 100, 100),
           Switch(canvas, 200, 100, False),
           LightBulb(canvas, 300, 100, False),
           AutomaticSwitch(canvas, 400, 100, False, 1000),
           Ammeter(canvas, 100, 200, 1),
           Voltmeter(canvas, 200, 200),
           Wattmeter(canvas, 300, 200),
           FrequencyMeter(canvas, 400, 200, 60)
           ]

# Connect elements
circuit[0].connectTo(circuit[1])
circuit[1].connectTo(circuit[2])
circuit[2].connectTo(circuit[3])
circuit[3].connectTo(circuit[4])
circuit[4].connectTo(circuit[5])
circuit[5].connectTo(circuit[6])
circuit[6].connectTo(circuit[7])

# Draw elements
drawCircuit(circuit)

# Calculate power
power = calculatePower(circuit)

# Print power
print("Power:", power)

# Main loop
window.mainloop()