

from rtlsdr import RtlSdr
import numpy as np
import hashlib
import time 

sdr = RtlSdr()
sdr.sample_rate = 2.048e6 # Hz
sdr.center_freq = 100e6   # Hz
sdr.freq_correction = 60  # PPM
sdr.gain = 'auto'

samples = sdr.read_samples(1024)



# for i in range(len(samples),len(samples) -1,64):
#     if i == 1:
#         print(samples[1]) #numpy array
#     sha3_512 = hashlib.sha3_512()
#     while chunk := samples[i]  # Read in 4096-byte chunks
#             sha3_512.update(chunk)
sha3_512 = hashlib.sha3_512()
sha3_512.update(samples.tobytes())


start_time = time.perf_counter()

hash_val = sha3_512.hexdigest()
end_time = time.perf_counter()

elap = end_time - start_time
print(f"SHA3-512 hash: {hash_val}")
print(f"elapsed time {elap}")





