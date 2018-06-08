import os
import re
print("Welcome to the File Organizer. \n \n \n This Program only works for files with the format \"eventName_YYYY_division_location_description.documentType\" \n (i.e. anatomy_2017_c_yale_key.pdf) \n \n Please note that the underscroes within the file name format are required for the organizer to work.")
ak = raw_input("\n Please acknowledge (press any key to continue)")
indir = raw_input("\n Enter the Absolute Directory Locaiton \n (i.e. 'C:\Users\Evan\Desktop\_COPY of UNORGANIZED\Anatomy and Physiology'): ")
# indir = "C:\Users\Evan\Desktop\_COPY of UNORGANIZED\Anatomy and Physiology"
nameMinusTail = ""
headLoc = -1
yearPattern = re.compile('.*[_]([1-2][0-9]{3})[_]')

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
      if ".ini" in f:
        pass
      else:
        f = str(f)
        print "\n" + f
        if "YYYY" in f:
          headLoc = f.index("_YYYY_")
          nameMinusTail = f[:headLoc].capitalize()
          print(nameMinusTail)
        else:
          m = re.match(yearPattern, f)
          headLoc = m.end() - 6
          nameMinusTail = f[:headLoc].capitalize()
          print(nameMinusTail)
        if not os.path.exists(indir + "\\"+ nameMinusTail):
          os.makedirs(indir + "\\"+ nameMinusTail)
        os.rename((indir + "\\" + f), (indir + "\\" + nameMinusTail + "\\" + f))
exit = raw_input("\n Exit (press any key to exit): ")