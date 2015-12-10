"""
******************************
Application: Turo Simple Database
Created By: Priya Mishra
File: PriyaPythonDB.py
Last Updated: 12/09/2015
******************************
"""

#import libraries
import sys, os
from copy import deepcopy

print "Welcome to our DB"

#initialize variables
i = 1
bg = 1
line =""
#dict is the current db
dict = {}
#masterdict is the db of all Begin blocks
masterdict = {i:dict}


#function used for all the commands
def perform( str ):
	global i
	global bg
	global line
	global dict
	global masterdict
	
	#line is the command entered, which is then split
	line = str	
	commandArray = line.split()

	#See the else statement below to find out the functionality of each command 

	#SET Command
	if commandArray[0] == "SET":  
		if len(commandArray) == 3:
			dict[commandArray[1]] = commandArray[2]
		else:
			print "USAGE: SET name value"
	#GET command
	elif commandArray[0] == "GET":
		if dict.has_key(commandArray[1]) and len(commandArray) == 2:
			print dict[commandArray[1]]
		else:
			 print "NULL"
	#UNSET command
	elif commandArray[0] == "UNSET": 
		if dict.has_key(commandArray[1]) and len(commandArray) == 2:
			del dict[commandArray[1]]
		else:
			print "USAGE: UNSET name"		
	#NUMEQUALTO command
	elif commandArray[0] == "NUMEQUALTO":
		if len(commandArray) == 2:
			lookmeup = dict.values()
			print lookmeup.count(commandArray[1])
		else:
			print "USAGE: NUMEEQUALTO value"
	#BEGIN command
	elif commandArray[0] == "BEGIN" and len(commandArray) == 1:
		bg += 1
		masterdict[i] = deepcopy(dict)
		i += 1
		#print i

	#ROLLBACK command	
	elif commandArray[0] == "ROLLBACK" and len(commandArray) == 1:
		if bg != 1:
							
			i -= 1

			if dict == masterdict[i]:
				print "NO TRANSACTION" 

			bg -= 1
			dict = deepcopy(masterdict[i])
			
		else:
			print "NOT IN TRANSACTION BLOCK, CANNOT ROLLBACK"
	#Commit command
	elif commandArray[0] == "COMMIT" and len(commandArray) == 1:
		
		if masterdict[1] == dict:
			print "NO TRANSACTION"
		i = 1
		bg = 1
		masterdict.clear()
		masterdict[i] = deepcopy(dict)
		
	#END ccommand
	elif commandArray[0] == "END":
		exit()
	
	#If command is entered wrong, display list of commands
	else:
		print("")
		print ("Supported Commands") 
		print ("SET name value --- sets name to value") 
		print ("GET name --- gets the value for given name")
		print ("UNSET name --- removes the name and value")
		print ("NUMEQUALTO value --- finds the number of names with given value")
		print ("END --- ends program")
		print ("BEGIN --- begins transaction block")
		print ("ROLLBACK --- reverses all transaction in current block")
		print ("COMMIT --- commits all transactions in all blocks") 
		print("")

#determine whether a file was redirected to the app(else), and if not take raw output(true) 
if os.isatty(file.fileno(sys.stdin)):
	while True:
		str = raw_input('What is thy bidding: ')
		perform( str )		
else: 
	for l in sys.stdin:  
		perform ( l )
	

	

