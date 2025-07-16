# bolchSphereCalc
## A class to calculate the Bloch sphere coordinates (X, Y, Z) for a given quantum state.
### Attributes:
- beta (float): The beta parameter for initializing the quantum state.
- teta (float): The teta parameter for initializing the quantum state.
- shots (int): The number of shots for the quantum circuit simulation. Default is 8000.
- X (float): The X coordinate on the Bloch sphere.
- Y (float): The Y coordinate on the Bloch sphere.
- Z (float): The Z coordinate on the Bloch sphere.
- qc (QuantumCircuit): The quantum circuit used for the calculations.
### Methods:
- initCircuit():
```
    Initializes the quantum circuit with the given beta and teta parameters.
```
- getProba(c):
```
    Calculates the probability difference between measurement outcomes '0' and '1'.
```
- initX():
```
    Initializes the X coordinate on the Bloch sphere by applying a Hadamard gate and measuring the circuit.
```
- initY():
```
    Initializes the Y coordinate on the Bloch sphere by applying an S-dagger gate, a Hadamard gate, and measuring the circuit.
```
- initZ():
```
    Initializes the Z coordinate on the Bloch sphere by measuring the circuit directly.
```
- initAll():
```
    Initializes all three coordinates (X, Y, Z) on the Bloch sphere.
```

# test
## A test program to check if bloch coordinates are good

- Args:
    - res: An object with attributes `X`, `Y`, and `Z` representing the result values.
    - expect: A list or tuple containing the expected values in the order [X, Z, Y].