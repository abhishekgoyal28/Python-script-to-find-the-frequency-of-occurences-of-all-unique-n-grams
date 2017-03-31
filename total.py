#!/usr/bin/enc python3
import os
import concattrain
pwd=os.getcwd()
files=[f for f in os.listdir(pwd) if f.endswith("_train")]
#print(files)
for x in range(len(files)):
	dor="python3 dict.py "+files[x]
	os.system(dor)
