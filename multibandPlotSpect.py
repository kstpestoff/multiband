
import iqsFunc as iq

import numpy as np

import os
import matplotlib.pyplot as plt
import numpy as np

chanQtty = 8
qtty = 128

fileNameIn = "multiband_test_signal_IDFT.pcm"

fileNameOut = [fileNameIn + ".chn." + str(x) + ".pcm" for x in range(chanQtty)]
fout = [open(fileNameOut[x], "rb") for x in range(chanQtty)]

dataRead = 0

idx = 0
ax = []

fig, ax = plt.subplots(int(chanQtty/2), 2)

for chnIdx in range(chanQtty):
    iqs = iq.Read(fout[chnIdx], qtty, np.float32)
    
    ax[chnIdx%int(chanQtty/2)][int(chnIdx/(chanQtty/2))].set_title("channel #"+str(chnIdx))

    spectrum = np.log10(abs(np.fft.fft(iqs)))
    spectrum = np.concatenate((spectrum[int(len(spectrum)/2)+1::],spectrum[:int(len(spectrum)/2):]))
    curFig = ax[chnIdx%int(chanQtty/2)][int(chnIdx/(chanQtty/2))].plot(spectrum)

    plt.setp(curFig, 'linewidth', 0.4)
plt.show()