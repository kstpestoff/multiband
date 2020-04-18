import multibandIqFuncs as iq
import numpy as np

import os
import matplotlib.pyplot as plt
import numpy as np

dftLen = 8000
fftQtty = 1
 
filePath = "signals/"
fileNameIn = "multiband_test_signal_IDFT.pcm"

fin = filePath + fileNameIn

fid = open(fin,"rb")

iqs = iq.Read(fid, dftLen*fftQtty, np.float32)

spectrum = np.log10(abs(np.fft.fft(iqs)))

#iq.PlotTime(spectrum)

curFig = plt.plot(np.arange(0, dftLen*fftQtty, 1), spectrum)

plt.setp(curFig, 'linewidth', 0.4)
plt.show()