import os, time, sys, shutil
import datetime
from stat import * 


#filepath = raw_input('Enter file path')
#print filepath
filepath = '/home/justin/Pictures/Test_Folder'
files = {}
for entry in os.listdir(filepath):
	pathname = os.path.join(filepath, entry)
	statInfo = os.stat(pathname)
	dateInfo = datetime.datetime.fromtimestamp(statInfo.st_mtime)
	# dateInfo.day does not include the leading zero in the day
	# this causes the order to not be correct when sorting, add at some point
	dateStr = str(dateInfo.year) + '-' + str(dateInfo.month) + '-' + str(dateInfo.day)
	
	# create dictionary with filename and date pairs
	if files.has_key(pathname):
		print 'File Dictionary already contains ',pathname
	else:
		#add to the dictionary
		files[pathname] = dateStr


# ********* stopped here *********** 
# sort list based on date
newD = sorted(files, key=files.__getitem__)
print newD
# ****************************

# ^ ----------------------------------------------------

# iterate through sorted list
# create new filename string
# check if a filename already exists
# os.rename(src, dest)



