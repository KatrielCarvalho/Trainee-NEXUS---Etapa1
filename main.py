import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

L = 20
redeSpins = np.random.randint(0, 2, size=(L, L)) * 2 - 1

im = ax.imshow(redeSpins)


plt.show()
