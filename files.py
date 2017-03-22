import os
import datetime

#Getting a directory from the user
directory = raw_input("Enter a directory (default is " + os.path.expanduser("~") + "\Documents): ")

#Default directory is the user's documents folder. 
if not directory:
	directory = os.path.expanduser("~") + "\Documents"
#Changing to the correct directory to save from having to process the directory as part of the file name repeatedly
os.chdir(directory)

for f in os.listdir(directory):
	#In my case I'm going to be using an operation to include today's date for the test but I included a simple test here to keep it short
	#Here I'm just testing to see if A. is a file and B. contains the attribute I'm looking for.
	if os.path.isfile(f) and "2017" in str(datetime.datetime.fromtimestamp(os.stat(f).st_mtime)):
	#I deleted what I'm doing with the files because its not important to what I'm trying to show here.
		print(f)
