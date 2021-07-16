import izhikevich_cells as izh
import matplotlib.pyplot as plt
import numpy as np

class ccCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        # define neuron parameters
        self.celltype = 'chattering cell'
        self.C = 50
        self.vr = -60
        self.vt = -40
        self.k = 1.5
        self.a = .03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25
        self.stimVal = stimVal
        
    def plotMyData(somecell, upLim = 1000):
        tau = somecell.tau
        n = somecell.n
        v = somecell.v
        celltype = somecell.celltype
    
        # Plot the results
        fig = plt.figure()
        plt.plot(tau*np.arange(0,n),v[0,:].transpose(), 'k-')
        plt.xlabel('Time Step')
        plt.xlim([0, upLim])
        plt.ylabel(celltype + ' Cell Response')
        plt.show()
        
myCell = ccCell(500)
myCell.simulate()
izh.plotMyData(myCell)