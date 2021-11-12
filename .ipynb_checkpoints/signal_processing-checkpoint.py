import scipy.signal as signal
import numpy as np

def detrend(s):
    return signal.detrend(s)

def band_filter(s, l = 0.01, h = 0.25, n = 5): 
    b, a = signal.butter(5, [l, h], btype = 'bandpass')
    return signal.lfilter(b, a, s)

def normalization(s): 
    std = np.sqrt((s ** 2).sum(axis=0))
    if std < np.finfo(float).eps: std = 1.  # avoid numerical problems
    s /= std
    return s
    
def denoise(s, l = 0.01, h = 0.25, n = 5):
    s = detrend(s)
    s = band_filter(s)
    s = normalization(s)
    