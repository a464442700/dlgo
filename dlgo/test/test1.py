import gzip
import pickle
from matplotlib import pyplot as plt

import numpy as np

path = '../nn/mnist.npz'
f = np.load(path)
x_train, y_train = f['x_train'], f['y_train']
x_test, y_test = f['x_test'], f['y_test']
f.close()
a=[ x_train[0]]
#print(a)
b=[np.reshape(x,(784,1)) for x in a]
#print(b)

plt.imshow(x_train[0])
plt.show()
print(y_train[0])
