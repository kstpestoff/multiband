import numpy as np
import multibandIqFuncs as iq

filePath = "signals/"
fileNameOut = "multiband_test_signal_IDFT.pcm"

fon = filePath + fileNameOut

fout = open(fon, "wb")

fileLen = int(50e6/2)

frec = 50000000         # receiver band
fsb = 6250              # signal bandwidth
dftLen = int(frec/fsb)  # signal grid

spect = np.zeros(dftLen,np.complex64)

spect[1::8] = 1 + 1j
spect[3000:5000:] = 0 


dataWriten = 0
while (fileLen-dataWriten >= dftLen):
    awgnI = np.random.normal(0.0, np.sqrt(10.0 ** (-8.50)), dftLen)
    awgnQ = np.random.normal(0.0, np.sqrt(10.0 ** (-8.50)), dftLen)

    iqs = np.fft.ifft(spect) + awgnI + 1j * awgnQ
    fout.write(np.complex64(iqs))
    dataWriten += dftLen
    print("dataWriten = %d (%.1f %%)" %(dataWriten, 100*dataWriten/fileLen))
    
fout.close()