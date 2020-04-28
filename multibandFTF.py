import multibandIqFuncs as iq
import numpy as np

import os

chanQtty = 32
 
filePath = "signals/"
fileNameIn = "multiband_test_signal_IDFT.pcm"

fin = filePath + fileNameIn

fileNameOut = [fin + ".chn." + str(x) + ".pcm" for x in range(chanQtty)]
fout = [open(fileNameOut[x], "wb") for x in range(chanQtty)]

fid = open(fin, "rb")

# signal params
sps = 4
signalBand = 50e6
freqSpacing = 6250

iqsQtty = int((signalBand / freqSpacing))
fileLen = int(os.path.getsize(fin) / 8)

dataRead = 0

idx = 0

signal = iq.Read(fid, iqsQtty, np.float32)

while len(signal) >= iqsQtty:

    spectrum =  np.fft.fft(signal)

    for chanIdx in range(chanQtty):    
        iq.Write(fout[chanIdx], spectrum[chanIdx]*np.exp(-1j*chanIdx*idx*2*np.pi/sps), 1, np.float32)

    signal = np.concatenate((signal[int(iqsQtty/sps)::],iq.Read(fid, int(iqsQtty/sps), np.float32)))
    idx = idx + 1
    dataRead += int(iqsQtty/sps)
    print("idx: %d, percent: %0.2f %%" % (idx, 100 * dataRead / fileLen))
   
fid.close()

for chanIdx in range(chanQtty):
    fout[chanIdx].close()
