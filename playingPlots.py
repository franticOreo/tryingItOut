#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


print("This is console module")



spins = []
game1_result = [8,24,32,24,33,19,5,12,14,32,7,22,5,8,6,28,32,23
        ,5,8,6,28,32,23,4,32,27,19,31,9,19,13]

game2_result = [36,5,20,7,18,13,7,4,28,2,36,34,
        34,32,19,33,27,31]



for i in range(1,33):
    spins.append(i)



print(len(result) == len(spins))


#print(len(result))
#print(len([1]))
#print(spins)
