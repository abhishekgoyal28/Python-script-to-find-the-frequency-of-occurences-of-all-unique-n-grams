#!/usr/bin/enc pyton3
#This script is for going in every directory and concatenating all text files in that directory
import os
#import subprocess
#print("-----------------------------------------------------------Hello user------------------------------------------------------\n")
pwd=os.getcwd()
#print(pwd)
#print("\n")
dir="/home/pirateking/Desktop/Sys_Programming_Lab/ADFA-LD/ADFA-LD/Attack_Data_Master"
os.chdir(".")
dir=os.getcwd()
#print(pwd)
#print("\n")
#os.system("ls -alt")
concat=""
#folder=int(input("\n Choose which folder you want to enter Adduser=1 Hydra_FTP=2 Hydra_SSH=3 Java_Meterpreter=4 Meterpreter=5 Web_Shell=6.\n"))
for folder in range(1,7):
	concat=""
	for subfolder in range(1,8):
		if folder==1:
			dir=dir+"/Adduser_"+str(subfolder)
		elif folder==2:
			dir=dir+"/Hydra_FTP_"+str(subfolder)
		elif folder==3:
			dir=dir+"/Hydra_SSH_"+str(subfolder)
		elif folder==4:
			dir=dir+"/Java_Meterpreter_"+str(subfolder)
		elif folder==5:
			dir=dir+"/Meterpreter_"+str(subfolder)
		elif folder==6:
			dir=dir+"/Web_Shell_"+str(subfolder)
		os.chdir(dir)
		#print(dir)
		#print("\n")
		filenames=os.listdir()
		length=len(filenames)
		for x in range(length):
			f=open(filenames[x],"r+")
			concat=concat+f.read()
			f.close()
		#print("\n")
		dir="/home/pirateking/Desktop/Sys_Programming_Lab/ADFA-LD/ADFA-LD/Attack_Data_Master"
	os.chdir("/home/pirateking/Desktop/Sys_Programming_Lab/ADFA-LD/ADFA-LD/Attack_Data_Master")
	if folder==1:
		filekanaam="Adduser"
	elif folder==2:
		filekanaam="Hydra_FTP"
	elif folder==3:
		filekanaam="Hydra_SSH"
	elif folder==4:
		filekanaam="Java_Meterpreter"
	elif folder==5:
		filekanaam="Meterpreter"
	elif folder==6:
		filekanaam="Web_Shell"
	filekanaam=filekanaam+"_train"
	f1=open(filekanaam,"w+")
	f1.write(concat)
	f1.close()
#print("--------------------------------------------------------------------------pirateking--------------------------------------------------------------------")

