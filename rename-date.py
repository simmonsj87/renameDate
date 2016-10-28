import os, time, sys, shutil
import datetime
from stat import * 
from operator import itemgetter


#filepath = raw_input('Enter file path')
#print filepath
filepath = '/home/justin/Pictures/Test_Folder'
files = {}
for entry in os.listdir(filepath):
	pathname = os.path.join(filepath, entry)
	statInfo = os.stat(pathname)
	dateInfo = datetime.datetime.fromtimestamp(statInfo.st_mtime)
	
	# dateInfo.day does not include the leading zero in the day
	# add leading zero to day
	if dateInfo.day < 10:
		dayString = '0' + str(dateInfo.day)
	else:
		dayString = str(dateInfo.day)
	# ------------------------
	# consider adding minute to this string to further sort
	# ------------------------	
	dateStr = str(dateInfo.year) + '-' + str(dateInfo.month) + '-' + dayString
	
	# create dictionary with filename and date pairs
	if files.has_key(pathname):
		print 'File Dictionary already contains ',pathname
	else:
		#add to the dictionary
		files[pathname] = dateStr



# sort list based on date

myFileList = files.items()

#sorted based on the date, which is the second value of the tuple in list
mySortedList = sorted(myFileList, key=itemgetter(1))

#accessing individual elements of the list
for i in range(len(mySortedList)):
	print mySortedList[i][0], mySortedList[i][1]

# ********* stopped here *********** 
# next steps
# loop through all files & dates
# set date as current
# call function to create new file name
# rename file
# ****************************

# iterate through sorted list
# create new filename string
# check if a filename already exists
# os.rename(src, dest)



