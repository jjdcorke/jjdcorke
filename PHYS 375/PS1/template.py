# For plotting
import matplotlib.pyplot as plt

# For file i/o and math
import numpy as np

# Enabling using LaTex for making labels pretty, not really necessary
from matplotlib import rc
rc('text', usetex=True)


# Read in data from a file called datafile.txt
data = np.loadtxt('W21_ps1_orbit.dat')

# Call the second and third columns x,y
x = data[:,1]
y = data[:,2]

# Plot a vector x vs y with a solid black line
plt.plot(x,y,'-k')

# Add some labels
plt.xlabel('x')
plt.ylabel('y')

# Save figure
plt.savefig('template.pdf')



