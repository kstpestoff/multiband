import matplotlib.pyplot as plt
import numpy as np

#plot iq signal
#
#
def PlotTime(iqs, qtty = -1):
    if qtty == -1:
        qtty = len(iqs)
    
    iqsFig = plt.plot(np.arange(0,qtty,1),iqs[0:qtty].real,np.arange(0,qtty,1),iqs[0:qtty].imag)
    plt.show()
    plt.setp(iqsFig, 'linewidth', 0.2 )
    return iqsFig

#rotate iq signal
#
#
def Rotate(iqs, fd, ferr, stPh = 0):
    lenIqs = len(iqs)
    phase = [1j*(k*2*np.pi*ferr/fd+stPh) for k in range(0,lenIqs)]
    iqRot = iqs*np.exp(phase)
    
    stPh = ((lenIqs-1)*2*np.pi*ferr/fd+stPh)

    return iqRot


#plot iq signal
#
#
def Plot(iqs, qtty = -1):
    if qtty == -1:
        qtty = len(iqs)

    iqsFig = plt.plot(iqs[0:qtty].real,iqs[0:qtty].imag,'.')
    plt.xlim([-1.1*max(abs(iqs[0:qtty])), 1.1*max(abs(iqs[0:qtty]))])
    plt.ylim([-1.1*max(abs(iqs[0:qtty])), 1.1*max(abs(iqs[0:qtty]))])
    plt.show()
    plt.setp(iqsFig, 'markersize', 1.0 )

    return iqsFig

#read iq signal from file
#
#
def Read(fid, qtty, dtype = np.int16):

    fileData = np.fromfile(fid, dtype, 2*qtty)
    return fileData[0:2*qtty:2] + 1j*fileData[1:2*qtty:2]

#write iq signal to file
#
#
def Write(fid, iq, iqqty,dtype=np.int16):
    if (iqqty == 1):
        if dtype == np.int16:           
            fid.write(np.int16(iq.real))
            fid.write(np.int16(iq.imag))

        if dtype == np.float32:
            fid.write(np.float32(iq.real))
            fid.write(np.float32(iq.imag))
        packLen = 1
    else:
        packLen = min(iqqty,len(iq))

        fileData = np.zeros(2*packLen, dtype)
        
        if dtype == np.int16:
            fileData[0:2*packLen:2] = np.int16(iq[0:packLen].real)
            fileData[1:2*packLen:2] = np.int16(iq[0:packLen].imag)

        if dtype == np.float32:
            fileData[0:2*packLen:2] = np.float32(iq[0:packLen].real)
            fileData[1:2*packLen:2] = np.float32(iq[0:packLen].imag)

        fid.write(fileData)
    return packLen


