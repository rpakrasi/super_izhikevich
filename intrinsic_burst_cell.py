import izhikevich_cells as izh
import matplotlib.pyplot as plt
import numpy as np

class ibCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        # define neuron parameters
        self.celltype = 'intrinsic burst'
        self.C = 150
        self.vr = -75
        self.vt = -45
        self.k = 1.5
        self.a = .01
        self.b = 5
        self.c = -56
        self.d = 130
        self.vpeak = 50
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
        
myCell = ibCell(1000)
myCell.simulate()
izh.plotMyData(myCell)