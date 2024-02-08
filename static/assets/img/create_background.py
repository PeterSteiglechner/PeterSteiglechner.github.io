import matplotlib.pyplot as plt

import numpy as np

X, Y = np.meshgrid(np.arange(0,1920), np.arange(0, 100))
fig, ax = plt.subplots(1,1, figsize=(19.2, 1))
plt.pcolormesh(X, Y, X, cmap="summer", vmin = 0,vmax=1920,)
fig.subplots_adjust(left=0, top=1, bottom=0, right=1)
fig.set_facecolor("y")
plt.savefig("background_summer.jpeg")