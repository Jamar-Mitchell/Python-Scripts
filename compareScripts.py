#! /usr/bin/python

import sys; 
import filecmp
from inspect import currentframe, getframeinfo
import os

file1 = 'testa.py'
file2 = 'testb.py'


def printdifferences(): 
	with open(file1, 'r') as script1:
		with open(file2, 'r') as script2:
			diff = set(script1).difference(script2)
			diff.discard('\n')
			print("The differences between "+file1+" and "+file2+ " are at the lines:\n")
			
			if len(diff)== 0 : 
				print("|No differences")
			else :
				for line in diff:
					print(line)
				print (">>> within file " +file1 +"\n")

def isIdentical():
	with open(file1, 'r') as script1:
		with open(file2, 'r') as script2:
			diff = set(script1).symmetric_difference(script2)
			if len(diff)== 0 : 
				return "True"
			else :
				return "False"

def numDifferences():
	with open(file1, 'r') as script1:
		with open(file2, 'r') as script2:
			diff = set(script1).difference(script2)
			return len(diff)

print("\nFiles are Identical: "+ isIdentical())
print("There are "+ str(numDifferences()) + " lines different in "+file1+" compared to "+file2)
printdifferences()
