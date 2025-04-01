import numpy as np
import matplotlib.pyplot as plt
from Sqveriki import Comp, upgrade_range

A = 0
B = 20
C = 1



exy = [A, B, C]

pover = len(upgrade_range(*exy)) ** 2



Zn = []

Z1 = 0 + 0j
for i in range(pover):
    for x in upgrade_range(*exy):
        for y in upgrade_range(*exy):
            Z1 = Comp(x, y)
            Zn.append(Z1.strange_step_complex(i))
Zn = np.array(Zn)



x = Zn.real
y = Zn.imag

plt.plot(x, y, "g*")

plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()
