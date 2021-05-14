#!/usr/bin/env python3

import psutil
import shutil

print("psutils and sutils imported")

print('Let us read the contents of the file text.txt')

with open('text.txt') as f:
	for line in f:
		print(line)
