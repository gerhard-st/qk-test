
from qiskit import *
from math import pi
#from qiskit.visualization import plot_bloch_multivector

# Let's do an X-gate on a |0> qubit
try:
    qc = QuantumCircuit(1)
except:
    print("-")

qc.x(0)
#qc.draw()

# Let's see the result
backend = Aer.get_backend('statevector_simulator')
out = execute(qc,backend).result().get_statevector()
print(out)
#plot_bloch_multivector(out)

