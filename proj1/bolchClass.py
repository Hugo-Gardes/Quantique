from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

backend = StatevectorSampler()

class bolchSphereCalc:
    def __init__(self, beta, teta, shots=8000):
        self.X = 0
        self.Y = 0
        self.Z = 0
        self.beta = beta
        self.teta = teta
        self.shots = shots
        self.qc = QuantumCircuit(1)
        self.initCircuit()

    def initCircuit(self):
        self.qc.initialize([self.beta, self.teta], 0)

    def getProba(self, c):
        p0 = c.get('0', 0) / self.shots
        p1 = c.get('1', 0) / self.shots
        return (p0 - p1)

    def initX(self):
        tmpCirc = self.qc.copy()
        tmpCirc.h(0)
        tmpCirc.measure_all()
        print("xCircuit:")
        print(tmpCirc.draw())
        res = backend.run([tmpCirc], shots=self.shots).result()[0] # ne pas utiliser aersim / use statevectorsample
        print(res.data)
        c = res.data.meas.get_counts()
        self.X = self.getProba(c)

    def initY(self):
        tmpCirc = self.qc.copy()
        tmpCirc.sdg(0)
        tmpCirc.h(0)
        tmpCirc.measure_all()
        print("yCircuit:")
        print(tmpCirc.draw())
        res = backend.run([tmpCirc], shots=self.shots).result()[0]
        print(res)
        c = res.data.meas.get_counts()
        self.Y = self.getProba(c)

    def initZ(self):
        tmpCirc = self.qc.copy()
        tmpCirc.measure_all()
        print("zCircuit:")
        print(tmpCirc.draw())
        res = backend.run([tmpCirc], shots=self.shots).result()[0]
        print(res)
        c = res.data.meas.get_counts()
        self.Z = self.getProba(c)

    def initAll(self):
        self.initZ()
        self.initX()
        self.initY()
