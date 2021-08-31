
from qiskit import *
from math import pi
#from qiskit.visualization import plot_bloch_multivector

backend = Aer.get_backend('statevector_simulator')

#
qc = QuantumCircuit(1,1)

#
qc.x(0)
out = execute(qc,backend).result().get_statevector()
print(qc)
print(out)

#
qc.h(0)
out = execute(qc,backend).result().get_statevector()
print(qc)
print(out)

#
qc.barrier()
qc.measure(0,0)
print(qc)
print(execute(qc,backend).result().get_statevector())

job = backend.run(qc, shots=1, memory=True)
output  = job.result().get_memory()[0]
#print(job.result())
print(output)
