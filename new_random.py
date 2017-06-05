import numpy as np
import matplotlib.pyplot as plt
import math

# Condition monitoring
def alert(x,y,z):
    for i in range(len(x)):
        if (x[i] == 0) and (y[i] == 0) and (z[i]==0):
            print x[i],y[i],z[i]
            print " Accident / Incident occured"
            return False
        if (x[i] <= 2) and (y[i] <= 2) and (z[i] <=2):
            if (x[i] == 2) and (y[i] == 2) and (z[i]==2):
                print x[i],y[i],z[i]
                print "high alert 95 % of failure"
            print x[i],y[i],z[i]
            print "high alert very critical situation"
        if (x[i] <= 4) and (y[i] <= 4) and (z[i] <= 4):
            print x[i],y[i],z[i]
            print "Red alert check for condition"
        if (x[i] >= 7) and (y[i] >= 7) and (z[i] >= 7):
            print x[i],y[i],z[i]
            print "Good to go condition"

def getRMSData(x,y,z):
	return [ math.sqrt((x[i]*x[i])+(y[i]*y[i])+(z[i]*z[i]))  for i in xrange(0,90)]
xyz = []
def loadEvents():
    x=  np.random.randint(10, size=(90))
    y =  np.random.randint(10, size=(90))
    z = np.random.randint(10, size=(90))
    xyz.append(z)
    rms = getRMSData(x,y,z)
    alerts = alert(x,y,z)
    print "No of Events recorded :",len(x)
    plt.plot (x, label="x")
    plt.plot (y, label="y")
    plt.plot (z, label="z")
    plt.plot (rms,  label="rms")
    plt.legend(loc='upper left')
    plt.show()

loadEvents()

# Display a sample signal with hanning window and after psd analysis
signal = np.array(xyz[0], dtype=float)
plt.subplot(2,2,1)
plt.plot(signal,label="normal signal")
plt.legend(loc='lower left')
plt.subplot(2,2,2)
plt.plot(signal* np.hanning(90),label="Signal after hanning window")
plt.legend(loc='lower left')
plt.figure()
fourier = np.fft.fft(signal*np.hanning(90))
n = signal.size-3
timestep = 0.000625
freq = np.fft.fftfreq(n, d=timestep)
psd = (fourier.real * fourier.real)/(1600*90)
psd  = np.array(psd, dtype=float)
psd[2:n-1] =  2* psd[2:n-1]
plt.plot(freq[2:n/2], 10*np.log10(psd[2:n/2]),label="Signal after psd analysis")
plt.scatter(freq[2:n/2], 10*np.log10(psd[2:n/2]))
plt.legend(loc='center left')
plt.show()
