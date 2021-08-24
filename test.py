
from qiskit import *
from math import pi
#from qiskit.visualization import plot_bloch_multivector

backend = Aer.get_backend('statevector_simulator')

#
qc = QuantumCircuit(1)

#
qc.x(0)
out = execute(qc,backend).result().get_statevector()
print(out)

#
qc.h(0)
out = execute(qc,backend).result().get_statevector()
print(out)

