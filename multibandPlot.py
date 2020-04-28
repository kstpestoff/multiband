import multibandIqFuncs as iq

import numpy as np

import os
import matplotlib.pyplot as plt
import numpy as np

chanQtty = 12
qtty = 256

filePath = "signals/"
fileNameIn = "multiband_test_signal_IDFT.pcm"

fin = filePath + fileNameIn

fileNameOut = [fin + ".chn." + str(x) + ".pcm" for x in range(chanQtty)]
fout = [open(fileNameOut[x], "rb") for x in range(chanQtty)]

dataRead = 0

idx = 0
ax = []

colQtty = 3

fig, ax = plt.subplots(int(chanQtty/colQtty), colQtty)

for chnIdx in range(chanQtty):
    iqs = iq.Read(fout[chnIdx], qtty, np.float32)
    
    curFig = ax[chnIdx%int(chanQtty/colQtty)][int(chnIdx/(chanQtty/colQtty))].plot(np.arange(0, qtty), iqs.real, np.arange(0, qtty), iqs.imag)

    ax[chnIdx%int(chanQtty/colQtty)][int(chnIdx/(chanQtty/colQtty))].set_title("channel #"+str(chnIdx))
    ax[chnIdx%int(chanQtty/colQtty)][int(chnIdx/(chanQtty/colQtty))].set_ylim((-1.5, 1.5))
    ax[chnIdx%int(chanQtty/colQtty)][int(chnIdx/(chanQtty/colQtty))].grid()

    plt.setp(curFig, 'linewidth', 0.4)

plt.show()

for chanIdx in range(chanQtty):
    fout[chanIdx].close()