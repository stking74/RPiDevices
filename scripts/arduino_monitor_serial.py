import RPiDevices
import time
import numpy as np

data = []
ard = RPiDevices.arduino.Arduino()
blankbit = False
ti = time.time()
print(ard.read().decode())
while True:
    av = int(ard.read().decode())
    print(av)
    if blankbit: blankbit = False
    else:
        data.append(av)
        blankbit = True
    if time.time() - ti > 60 * 15:
        data = np.array(data)
        fname = str(time.time())+ '.npy'
        with open(fname, 'wb') as f:
            np.save(f, data)
        data = []
        ti = time.time()
