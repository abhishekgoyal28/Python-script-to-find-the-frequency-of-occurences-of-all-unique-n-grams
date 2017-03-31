#!/usr/bin/enc pyton3
#This script is for going in every directory and concatenating all text files in that directory
import os
import subprocess
print("-----------------------------------------------------------Hello user------------------------------------------------------\n")
#pwd=os.getcwd()
#print(pwd)
filenames=os.listdir()
#print(filenames)
length=len(filenames)
concat=""
for x in range(length):
	if filenames[x]!="concat_all.py":
		f=open(filenames[x],"r+")
		concat=concat+f.read()
		f.close()
f1=open("Training_train","w+")
f1.write(concat)
f1.read()
f1.close()
print("--------------------------------------------------------------------------pirateking--------------------------------------------------------------------")

