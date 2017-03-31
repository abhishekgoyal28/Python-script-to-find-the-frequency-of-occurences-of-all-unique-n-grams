#!/usr/bin/enc pyton3
#This script is for just determining different n-tuples in the file
import os
import sys
from operator import itemgetter
arg=sys.argv[1]
#print("Hello user\n")
#n=int(input("Which n-tuple do you want 3,5 or 7?\n"))
#pwd=os.getcwd()
#print(pwd)
#print("\n")
dir="/home/pirateking/Desktop/Sys_Programming_Lab/ADFA-LD/ADFA-LD/Attack_Data_Master"
os.chdir(".")
#pwd=os.getcwd()
#print(pwd)
#print("\n")
#os.chdir("/home/pirateking/Desktop/Sys_Programming_Lab/ADFA-LD/ADFA-LD/Training_Data_Master")
f = open(arg,"r+")
lines=f.readlines()
data=""
data=data+lines[0]
#print(data)
#print("\n")
tup=data.split()
#print("\n")
f.close()
variable=int(len(tup))
#print(variable)
#print("\n")
lost=[3,5,7]
jarg=""
for n in lost:
	variable=variable-(n-1)
	def grouper(k, iterable):
	    return [tup[i:i+k] for i in range(0,variable)]
	final=grouper(n,tup)
	final=list(map(tuple,final))
	faltu=[0,]*len(final)
	dictfinal=dict(zip(final,faltu))
	for w in final:
		if w in dictfinal:
			dictfinal[w]+=1
	newlist=[v for k,v in dictfinal.items()]
	newlist.sort()
	newlist.reverse()
	length=len(newlist)//3
	minimum=newlist[length]
	finallist=[[k,v] for k,v in dictfinal.items() if v>=minimum]
	finallist=sorted(finallist,key=itemgetter(1),reverse=True)
	#for x in range(len(finallist)):
	#	print(finallist[x],"\n")
	jarg=arg+"_result_"+str(n)
	f1=open(jarg,"w+")
	writedata=""
	for x in range(len(finallist)):
		writedata=str(finallist[x][0])+"------>"+str(finallist[x][1])+"\n"
		f1.write(writedata)
	f1.close()	
#dicfreq=[v for k,v in dictfinal.iteritems()]
#length=len(dicfreq)//3
#minimum=dictfreq[length]
#finalfinal=[[k,v] for k,v in dictfinal.iteritems() if v>=minimum]
#print(finalfinal)
#for w in final:
#	if w in fast
#print(final)
#print(len(final))
#backup=grouper(n,tup)
#print("\n")
#print(final)
#print("\n")
#uniq_final=[list(t) for t in set(map(tuple,final))]
#print(uniq_final)
#print("\n")
#print(len(uniq_final))
#print("\n")
#uniq_freq=[]
#for w in uniq_final:
#	uniq_freq.append(final.count(w))
#print(uniq_freq)
#print("\n")
#print(len(uniq_freq))
#print("\n")
#finalfreq=[0,]*len(uniq_freq)
#for x in range(len(uniq_freq)):
#	finalfreq[x]=uniq_freq[x]
#finalfreq.sort()
#finalfreq.reverse()
#length=len(finalfreq)//3
#minimum=finalfreq[length]
#arg=arg+"_result_"+str(n)
#mydict=dict(zip(uniq_final,uniq_freq))
#newlist=sorted(mydict,key=itemgetter(1),reverse=True)
#print(newlist[0])
#print("\n",length)
#f1=open(arg,"w+")
#writedata=""
#for x in range(len(finalfreq)):
#	if uniq_freq[x]>=minimum:
#		print(uniq_final[x],"---->",uniq_freq[x])
#		writedata=str(uniq_final[x])+"---->"+str(uniq_freq[x])+"\n"
#		f1.write(writedata)
#f1.close()
