#!/usr/bin/python
##
## Roozbeh Dehghannasiri.  09-11-2012
## Edited by Nolan Bentley. 05-22-2014
## This scripts converts finds matches between two columns of two different files
##

import csv                                                                                                                                               
import sys
import array
import os
from time import strftime
import time
                                                                                                                          
# Check for options
if len(sys.argv) != 6 :
	#tmpArr = sys.argv[0].split("/")
	print ("\nUsage : [input file 1] [file 1 column ] [input file 2] [file 2 column ] [output file] \n")
	print ("This script finds a match for the column number indicated for file 1 in the column number indicated for file 2.")
	print ("If a match is found, then it takes the entire line of information from file 2 and appends it to the end of the line in file 1." )
	print ("If a match cannot be found between the columns of file 1 and file 2, it just moves to the next line.")
	print ("When all rows of file 1 have been completed, then it writes the output to the new file name that is provided on the command line.")
	sys.exit()
input_file_name1 = sys.argv[1]
input_file_name2 = sys.argv[3]
output_file_name = sys.argv[5]	
if not os.path.exists(input_file_name1):
		print ("Error!\nThe input file does not exist.\n")
		sys.exit()
if not os.path.exists(input_file_name2):
		print ("Error!\nThe input file does not exist.\n")
		sys.exit()

print ("=> Reading an input file...")

column1 = sys.argv[2]
column1 = int(column1)
column2 = sys.argv[4] 
column2 = int(column2)
column1 = column1 -	1
column2 = column2 -	1


input1 = open(input_file_name1, 'r')
input2 = open(input_file_name2, 'r')
file_in1 = csv.reader(input1)
file_in2 = csv.reader(input2)
roozbeh = open(output_file_name, 'w')
file_out = csv.writer(roozbeh)

numrow1 = 0
numrow2 = 0
for a in file_in1:
	for c in file_in2:	
		if numrow1 == 0:
			if numrow2 == 0:
				del a[37:62]
				file_out.writerow(a+c)
				numrow1 = 1
				numrow2 = 1
		
input2.seek(0)
input1.seek(0)
numrow1 = 0
for a in file_in1:
	numrow1 = numrow1 + 1
	if numrow1 >= 2:
		flag = 0
		numrow2 = 0
		input2.seek(0)
		for c in file_in2:
			numrow2 = numrow2 + 1
			if numrow2 >= 2:
				if a[column1] == c[column2]:
					del a[37:62]
					file_out.writerow(a + c)
					flag = 1
					break
		if flag == 0:
			file_out.writerow(a)
roozbeh.close()
input1.close()
input2.close()

			


    
