from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram
# Creating registers
q = QuantumRegister(name='q', size=3)
c = ClassicalRegister(name='c', size=3)
# Creates the quantum circuit
teleport = QuantumCircuit(q, c)
# Step 0 - Instantiate qubit 0 in the state to be teleported:
teleport.ry(1.5708, q[0])  # Apply rotation around the Y-axis
teleport.rz(3.14159, q[0]) # Apply rotation around the Z-axis

teleport.barrier() # just a visual aid

# Step 1 - Make the shared entangled state in between qubit 1 and qubit 2
teleport.h(q[1])
teleport.cx(q[1], q[2])

teleport.barrier() # just a visual aid
# Step 2 & 3: Alice applies a series of gates on qubit 0 and qubit 1
teleport.cx(q[0], q[1])
teleport.h(q[0])


# Step 4 - Alice measures qubit 0 and qubit 1
teleport.measure(q[0], c[0])
teleport.measure(q[1], c[1])

# Step 5 - Bob applies a unitary transformation on his qubit
# based on the outcome of Alice's measurements
teleport.x(q[2]).c_if(c, 1)
teleport.z(q[2]).c_if(c, 2)

teleport.barrier() # just a visual aid

# Step 6 - Bob checks if he got the right state
teleport.measure(q[2], c[2])

# Visualizing your teleportation circuit
teleport.draw()

backend = BasicSimulator()
result = backend.run(teleport, shots=8192).result()
counts = result.get_counts()
print(f"The counts for circuit teleport are: {counts}")
plot_histogram(counts)