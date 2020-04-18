import multibandIqFuncs as iq
import numpy as np

import os

chanQtty = 32

fileNameIn = "multiband_test_signal_IDFT.pcm"

fileNameOut = [fileNameIn + ".chn." + str(x) + ".pcm" for x in range(chanQtty)]
fout = [open(fileNameOut[x], "wb") for x in range(chanQtty)]

fin = open(fileNameIn, "rb")

# signal params
sps = 16
signalBand = 50e6
freqSpacing = 6250

iqsQtty = int((signalBand / freqSpacing))
fileLen = int(os.path.getsize(fileNameIn) / 8)

dataRead = 0

idx = 0

signal = iq.Read(fin, iqsQtty, np.float32)

while len(signal) >= iqsQtty:

    spectrum =  np.fft.fft(signal)

    for chanIdx in range(chanQtty):    
        iq.Write(fout[chanIdx], spectrum[chanIdx], 1, np.float32)

    signal = np.concatenate((signal[:iqsQtty-int(iqsQtty/sps):],iq.Read(fin, int(iqsQtty/sps), np.float32)))
    idx = idx + 1
    dataRead += int(iqsQtty/sps)
    print("idx: %d, percent: %0.1f" % (idx, 100 * dataRead / fileLen))

fin.close()

for chanIdx in range(chanQtty):
    fout[chanIdx].close()
