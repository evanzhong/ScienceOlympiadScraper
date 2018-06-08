import os
print("Welcome to the File Organizer. \n \n \n This Program only works for files with the format \"eventName_YYYY_division_location_description.documentType\" \n (i.e. anatomy_2017_c_yale_key.pdf) \n \n Please note that the underscroes within the file name format are required for the organizer to work.")
ak = raw_input("\n Please acknowledge (press any key to continue)")
indir = raw_input("\n Enter the Absolute Directory Locaiton \n (i.e. 'C:\Users\Evan\Desktop\_COPY of UNORGANIZED\Anatomy and Physiology'): ")
# indir = "C:\Users\Evan\Desktop\_COPY of UNORGANIZED\Anatomy and Physiology"
nameMinusTail = ""
fileHead = raw_input("\n Enter the File Header in the form _YYYY_ \n (i.e. _2017_): ")
headLoc = -1
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
      if ".ini" in f:
        pass
      else:
        print(f)
        headLoc = f.index(fileHead)
        nameMinusTail = f[:headLoc].capitalize()
        print(nameMinusTail)
        if not os.path.exists(indir + "\\"+ nameMinusTail):
          os.makedirs(indir + "\\"+ nameMinusTail)
        os.rename((indir + "\\" + f), (indir + "\\" + nameMinusTail + "\\" + f))
exit = raw_input("\n Exit (press any key to exit): ")