class Gate:
    def __init__(self, output):
        self.output = output

    def draw(self):
        pass

class AndGate(Gate):
    def __init__(self, input1, input2, output):
        Gate.__init__(self, output)
        self.input1 = input1
        self.input2 = input2

    def draw(self):
        print(self.input1, " ----|")
        print("       |----[ AND ]----", self.output)
        print(self.input2, " ----|")
        print()

class OrGate(Gate):
    def __init__(self, input1, input2, output):
        Gate.__init__(self, output)
        self.input1 = input1
        self.input2 = input2

    def draw(self):
        print(self.input1, " ----|")
        print("       |----[ OR ]----", self.output)
        print(self.input2, " ----|")
        print()

class NotGate(Gate):
    def __init__(self, input1, output):
        Gate.__init__(self, output)
        self.input1 = input1

    def draw(self):
        print(self.input1, " ----[ NOT ]----", self.output)
        print()

class NandGate(Gate):
    def __init__(self, input1, input2, output):
        Gate.__init__(self, output)
        self.input1 = input1
        self.input2 = input2

    def draw(self):
        print(self.input1, " ----|")
        print("       |----[ NAND ]----", self.output)
        print(self.input2, " ----|")
        print()

class NorGate(Gate):
    def __init__(self, input1, input2, output):
        Gate.__init__(self, output)
        self.input1 = input1
        self.input2 = input2

    def draw(self):
        print(self.input1, " ----|")
        print("       |----[ NOR ]----", self.output)
        print(self.input2, " ----|")
        print()

class Synthesizer:
    def gate_synthesize(self, code):
        code = code.lower()
        left, right = code.split("=")
        output = left.strip()
        right = right.strip()
        if " and " in right:
            a, b = right.split(" and ")
            gate = AndGate(a, b, output)

        elif " or " in right:
            a, b = right.split(" or ")
            gate = OrGate(a, b, output)

        elif " nand " in right:
            a, b = right.split(" nand ")
            gate = NandGate(a, b, output)

        elif " nor " in right:
            a, b = right.split(" nor ")
            gate = NorGate(a, b, output)

        elif right.startswith("not "):
            a = right.replace("not ", "")
            gate = NotGate(a, output)

        else:
            print("Invalid Input")
            return

        print("\nBehavioral Model :", code)
        print("Synthesized Circuit :\n")
        gate.draw()
    
    def boolean_synthesize(self, code):
        code=code.lower()
        left, right = code.split("=")
        output = left.strip()
        right = right.strip()

        #a.b+c
        if "." in right and "+" in right and right.count(".")==1:
            part1, part2 = right.split("+")
            a, b = part1.split(".")
            c = part2.strip()
            temp = "x1"
            print("\nBoolean Expression :", code)
            print("Synthesised Circuit :\n")

            gate1 = AndGate(a.strip(), b.strip(), temp)
            gate1.draw()

            gate2 = OrGate(temp, c, output)
            gate2.draw()

        #a+b.c
        elif "+" in right and "." in right and right.count(".")==1:
            part1, part2 = right.split("+")
            b, c = part2.split(".")
            a = part1.strip()
            temp = "x1"
            print("\nBoolean Expression :", code)
            print("Synthesised Circuit :\n")

            gate1 = AndGate(b.strip(), c.strip(), temp)
            gate1.draw()

            gate2 = OrGate(a, temp, output)
            gate2.draw()

        #a.b.c
        elif right.count(".") == 2 and "+" not in right:
            a,b,c = right.split(".")
            temp = "x1"

            print("\nBoolean Expression :", code)
            print("Synthesized Circuit :\n")

            gate1 = AndGate(a.strip(), b.strip(), temp)
            gate1.draw()

            gate2 = AndGate(temp, c.strip(), output)
            gate2.draw()

        #a+b+c
        elif right.count("+") == 2 and "." not in right:
            a,b,c = right.split("+")
            temp= "x1"

            print("\nBoolean Expression :", code)
            print("Synthesized Circuit :\n")

            gate1 = OrGate(a.strip(), b.strip(), temp)
            gate1.draw()

            gate2 = OrGate(temp, c.strip(), output)
            gate2.draw()

        #a.b+b.c+c.a
        elif right.count("+") ==2 and right.count(".") ==3:
            part1, part2, part3 = right.split("+")

            a,b = part1.split(".")
            b,c = part2.split(".")
            c,a = part3.split(".")

            temp1 = "x1"
            temp2 = "x2"
            temp3 = "x3"
            temp4 = "x4"

            print("\nBoolean Expression :", code)
            print("Synthesized Circuit :\n")

            gate1 = AndGate(a.strip(), b.strip(), temp1)
            gate1.draw()

            gate2 = AndGate(b.strip(), c.strip(), temp2)
            gate2.draw()

            gate3 = AndGate(c.strip(), a.strip(), temp3)
            gate3.draw()

            gate4 = OrGate(temp1, temp2, temp4)
            gate4.draw()

            gate5 = OrGate(temp4, temp3, output)
            gate5.draw()

        #xor gate
        elif " xor " in right or right == "ab'+a'b":

            temp1 = "x1"
            temp2 = "x2"
            nota = "na"
            notb = "nb"

            print("\nXOR Circuit:\n")

            gate1 = NotGate("a", nota)
            gate2 = NotGate("b", notb)

            gate3 = AndGate("a", notb, temp1)
            gate4 = AndGate(nota, "b", temp2)

            gate5 = OrGate(temp1, temp2, output)

            gate1.draw()
            gate2.draw()
            gate3.draw()
            gate4.draw()
            gate5.draw()

obj = Synthesizer()

#obj.gate_synthesize("y = not b")
obj.boolean_synthesize("y = a xor b")
