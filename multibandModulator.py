import numpy as np
import multibandIqFuncs as iq

outF = "multiband_test_signal.pcm"
fout = open(outF, "wb")

fileLen = int(50e6 / 2)

frec = 50000000             # receiver band
fg = 6250000                # guard
fstep = int(100000 / 2)     # test signal step
exp = np.ones(fileLen,complex)

awgnI = np.random.normal(0.0, np.sqrt(10.0 ** (-4.50)), len(exp))
awgnQ = np.random.normal(0.0, np.sqrt(10.0 ** (-4.50)), len(exp))

iqs1 = exp + awgnI + 1j * awgnQ

rotIq = np.zeros(fileLen,complex)

for freqOff in range(-int(frec / 2) + fg, int(frec / 2) - fg, fstep):
    rotIq = rotIq + iq.Rotate(iqs1, frec, freqOff, 0)
    print("idx = %d" % freqOff)

maxAmpl = max(abs(rotIq))
fout.write(np.complex64(rotIq) / maxAmpl)

fout.close()