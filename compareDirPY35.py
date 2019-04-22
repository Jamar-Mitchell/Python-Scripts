#! /usr/bin/python35

import sys; 
import filecmp
import os
import glob
import hashlib


########################################

def md5(fname):
    hash_md5 = hashlib.md5()
    
    with open(fname,"rb") as f:
    	for chunk in iter(lambda: f.read(2 ** 20), b""):
    		hash_md5.update(chunk)

    return hash_md5.hexdigest()

def populateDictionary(dirx,dictx,dirp):
	#must populate first before printDictionaries or findDifferences
	permDen=0
	try:
		for filename in dirx:
			dictx.update({filename : md5(filename)})

	except:
		permDen+=1
		print("The file/folder: " +str(filename)+ " was denied")

	if(permDen!=0):
		print("There are "+str(permDen)+" file(s) that were denied permission in " +str(dirp))

def printDictionaries(dict1,dict2):
	print("\nDictionaries:")
	print("Directory: "+str(dir1a))
	print(dict1 )
	print("\n")

	print("Directory: "+str(dir2a))
	print(dict2 )
	

def findDifferences(dict1,dict2):
	dict1Names=[]
	dict2Names=[]
	checksync1=[]
	checksync2=[]

	for x in dict1.values():
		dict1Names.append(x)

	for x in dict2.values():
		dict2Names.append(x)

	diff= set(dict1Names).difference(dict2Names)
	diff2= set(dict2Names).difference(dict1Names)

	#print("\nThe Differences in the directories are:\n")
	
	for x in diff:
		if (x in dict1.values()):
			res= list(dict1.keys())[list(dict1.values()).index(x)]
			checksync1.append(os.path.basename(res))

	for x in diff2:
		if (x in dict2.values()):
			res= list(dict2.keys())[list(dict2.values()).index(x)]
			checksync2.append(os.path.basename(res))

	d1=set(checksync1).difference(checksync2)
	d2=set(checksync2).difference(checksync1)
	outsync=set(checksync1).intersection(checksync2)

	print("Total differences between the two directories: "+ str(len(d1)+len(d2)+len(outsync)))

	print("\nFiles only in directory: "+str(dir1a))
	if(len(d1)==0):
		print("None")
	else:
		for x in d1:
			#print the value/ comment out if using big dir
			print(x)
			pass

	print("|count: "+str(len(d1)))

	print("\nFiles only in directory: "+ str(dir2a))
	if(len(d2)==0):
		print("None")
	else:
		for x in d2:
			#print the value/ comment out if using big dir
			print(x)
			pass

	print("|count: "+str(len(d2)))

	print("\nOut of sync files between the two directories:")
	if(len(outsync)==0):
		print("None")
	else:
		for x in outsync:
			#print the value/ comment out if using big dir
			print(x)

	print("|count: "+str(len(outsync)))

	return "\n"

#################################################
###SETTINGS
dir1a="/home/asd/mija"
dir2a="/home/asd/gvod/Packaged/NCCF/3_PythonToLocalDb"
filtertype =".*"
#recursive implementation s="/**/*"
s="/*"
##################################################
###MAIN
dir1 = glob.glob(dir1a+s+filtertype,recursive=True)
dir2 = glob.glob(dir2a+s+filtertype,recursive=True)

dict1= {}
dict2= {}

print("")
populateDictionary(dir1,dict1,dir1a)
populateDictionary(dir2,dict2,dir2a)

#printDictionaries(dict1,dict2)

print(findDifferences(dict1,dict2))

