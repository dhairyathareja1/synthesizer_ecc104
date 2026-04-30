# Digital Logic Synthesizer in Python

## Features Implemented

### 1. Gate Synthesis

Displays the schematic of a gate on entering the type.

#### AND Gate

#### OR Gate

#### NOT Gate

#### NAND Gate

#### NOR Gate

### 2. Boolean Function Synthesis

Displays the schematic corresponding to some basic boolean functions.

#### a.b+c

#### a+b.c

#### a.b.c

#### a+b+c

#### a.b + b.c + c.a

#### xor gate / ab'+a'b

## Code Structure

Divided the codebase into multiple classes and I have used inheritance between classes.

### Classes Implemented

1. Gate (Base Class) <br>
   a. And Gate <br>
   b. OrGate <br>
   c. NotGate <br>
   d. NandGate <br>
   e. NorGate <br>
2. Synthesizer

### Fucntions Implemented

1. gate_synthesize()
   Used for synthesis of direct gate expressions.

2. boolean_synthesize()
   Used for synthesis of simple Boolean algebra expressions.
