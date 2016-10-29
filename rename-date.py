#!/usr/bin/python

import os, time, sys, shutil, re
import datetime, imghdr, platform
import Tkinter
from stat import * 
from operator import itemgetter 

# ACTION: prompt user for name & date range
# Append descriptor to filename

userDescription = ''
userDescription = raw_input('Enter file description (press enter when done): ')
if re.search('[!@#$%\^&*,./;:\'"]', userDescription):
	print 'Invalid user description'
	# ACTION: Additional bonus points to simply remove bad characters
	userDescription = ''
if len(userDescription) > 0:
	userDescription = userDescription + ' '

filepath = '/home/justin/Pictures/Test_Folder'
fileDict = {}
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files: # replace '.' with filepath
	pathname = os.path.join('.', f)
	if (imghdr.what(pathname) is None): 
		continue	
	statInfo = os.stat(pathname)
	if (platform.system() == 'Windows'):
		dateInfo = datetime.datetime.fromtimestamp(statInfo.st_ctime)
	else:
		# System is likely Linux
		dateInfo = datetime.datetime.fromtimestamp(statInfo.st_mtime)

	dateStr = '{:%Y-%m-%d_%H:%M:%S}'.format(dateInfo)
	
	# create dictionary with filename and date pairs
	if fileDict.has_key(pathname):
		print 'File Dictionary already contains ',pathname
	else:
		#add to the dictionary
		fileDict[pathname] = dateStr

# create list from dictionary
myFileList = fileDict.items()

#sorted based on the date, which is the second value of the tuple in list
mySortedList = sorted(myFileList, key=itemgetter(1))


iterDate = None
count = 0

for i in range(len(mySortedList)):	
	if(iterDate == mySortedList[i][1][:10]):
		index = index + 1
	else:
		index = 1
	iterDate = mySortedList[i][1][:10]
	# ACTION: possibly turn this into a function to re-use later
	newFileName = os.path.join('.', userDescription + iterDate + '(' + "%03d"%index + ')')
	os.rename(mySortedList[i][0], newFileName)
	count = count + 1

print 'Number of files renamed: ',count



