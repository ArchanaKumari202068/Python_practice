"""
matplotlib --> mat plot lib

we can use anything instead of np
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 3*np.pi,1)
# y= np.sin(x)

y_sin =np.cos(x)
y_cos =np.sin(x)

plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine graph')
plt.legend(['sin','cos'])
plt.show()