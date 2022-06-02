from matplotlib import pyplot as plt

import numpy as np
m1=np.zeros((3,3))
m1[0][0]=1
m1[1][1]=1
m1[2][2]=1
#print(m1)
m2=np.reshape(m1, (9, 1))
#print(m2)

print('---')
a=[[1,0,0],[0,1,0],[0,0,1]]
# b=[np.reshape(x,(9,1)) for x in a]
# print(b)
# c=[5,6]
# zipb_c=zip(b,c)
# print(list(zipb_c))
plt.imshow(a)
plt.show()