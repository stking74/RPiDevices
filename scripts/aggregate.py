import numpy as np
import os
import datetime

data = {}
for item in os.listdir():
	if '.npy' in item:
	ts = float(item[:-4])
	with open(item, 'rb') as f:
		data[ts] = np.load(f)

keys = list(data.keys())
skeys = np.sort(keys)
sdata = [data[k] for k in skeys]

def apply_tags(data, timestamp, resolution=1):
	len_data = len(data)
	ti = timestamp - (len_data * resolution)
	tagged = [[],[]]
	for i, d in enumerate(data):
		ts = ti + (i * resolution)
		tagged[0].append(ts)
		tagged[1].append(d)
	x, y = tagged
	return x, y

tagged = []
for i, d in enumerate(sdata):
	