import os
print("Welcome to the File Organizer. \n \n \n This Program only works for files with the format \"eventName_YYYY_division_location_description.documentType\" \n (i.e. anatomy_2017_c_yale_key.pdf) \n \n Please note that the underscroes within the file name format are required for the organizer to work.")
ak = raw_input("\n Please acknowledge (press any key to continue)")
indir = raw_input("\n Enter the Absolute Directory Locaiton \n (i.e. 'C:\Users\Evan\Desktop\_COPY of UNORGANIZED\Anatomy and Physiology'): ")
# indir = "C:\Users\Evan\Desktop\_COPY of UNORGANIZED\Anatomy and Physiology"
fileHead = raw_input("\n Enter the File Header in the format eventName_YYYY_ \n (i.e. anatomy_2017_): ")
nameMinusHead = ""
HeadLocation = len(fileHead)
lastUnderscore = -1
CCLocation = -1
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
    	print f
        nameMinusHead = f[HeadLocation:]
        print nameMinusHead
        if ".ini" in f:
        	pass
        elif "captainstryouts" not in nameMinusHead:
        	nameMinusHead = nameMinusHead[2:]
        	print nameMinusHead
        	try:
        		lastUnderscore = nameMinusHead.index("_")
        		nameMinusHead = nameMinusHead[:lastUnderscore].capitalize() + " Invitational"
        		print nameMinusHead
        		print "\n"
        		if not os.path.exists(indir + "\\"+ nameMinusHead):
        			os.makedirs(indir + "\\"+ nameMinusHead)
        		os.rename((indir + "\\" + f), (indir + "\\" + nameMinusHead + "\\" + f))
        	except Exception as e:
        		raise
      	else:
      		nameMinusHead = nameMinusHead[2:]
      		print nameMinusHead
      		try:
      			CCLocation = nameMinusHead.index("captainstryouts-") + 16
      			lastUnderscore = nameMinusHead.index("_")
      			nameMinusHead = nameMinusHead[CCLocation:lastUnderscore].capitalize() + " Captains Tryouts"
      			print nameMinusHead
      			print "\n"
      			if not os.path.exists(indir + "\\"+ nameMinusHead):
        			os.makedirs(indir + "\\"+ nameMinusHead)
        		os.rename((indir + "\\" + f), (indir + "\\" + nameMinusHead + "\\" + f))
      		except Exception as e:
      			raise e
exit = raw_input("\n Exit (press any key to exit): ")