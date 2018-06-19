from matplotlib import pylab
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []
 
for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

#pylab.figure('lin')
pylab.plot(mySamples, myLinear)
pylab.show()
#plt.plot(mySamples, myQuadratic)
#plt.plot(mySamples, myCubic)
#plt.plot(mySamples, myExponential)
#
#plt.figure('lin')
#plt.plot(mySamples, myLinear)
