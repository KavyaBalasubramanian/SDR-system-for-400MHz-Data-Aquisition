import numpy, scipy
import os
import matplotlib.pyplot as plt

path = r'/home/beacon/Documents/GNUradio'
os.chdir(path)

samples = scipy.fromfile(open("data.fc32"), dtype=scipy.complex64)

digital_power_of_samples = numpy.abs(samples)**2
mean_power = digital_power_of_samples.mean()
max_power = max(digital_power_of_samples)

print (mean_power, max_power)
print (numpy.var(samples.real), numpy.var(samples.imag))
print ("Check")

real = numpy.real(samples)
imag = numpy.imag(samples)
plt.ylim([-1,1])
plt.xlim([-1,1])
plt.plot(real, imag)
plt.show()
