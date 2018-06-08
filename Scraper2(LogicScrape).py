""" Noted 1/13/18 that ggpSib does not account for all headers that contain years, merely only the headers that are 5 levels above the level of the link. Certain headers are only 4 levels above, while other are on the same level but an additional sibling up
	This was deemd an acceptable loss in data and therefore not corrected
"""
ack = raw_input("\n Welcome to the SciOly Python web scraper. This version scrapes from \"https://scioly.org/wiki/index.php/Test_Exchange_Archive\", and was written in January 2018. This scraper will download all files into a folder named raw_data, or create on if it does not exist in the directory of the this \".py\" file. A run log by the name of \"Scraper2Log.txt\" will also be created in the raw_data directory. Please check that the webpage has not changed from its January 2018 version to ensure that the webscraper will scrape sucessfully. \n\n This program requires the libraries: urllib2, wget, os, re and BeautifulSoup. \n\n Continue? (y/n): ")
import urllib2
import wget
import os
import re
from bs4 import BeautifulSoup

triggers = ["Station", "station", "Key", "key", "Test", "test", "Exam", "exam", "Sheet", "sheet", "Image", "image", "Answer", "answer", "Invvitational", "invitational", "Regional", "regional", "State", "state", "National", "national" "Solution", "solution", "Set",  "set", "Powerpoint", "PowerPoint", "powerpoint", "Quiz", "quiz", "Table", "table", "Figure", "figure", "Picture", "picture", "Part", "part", "Task", "task", "Rubric", "rubric", "Chart", "chart", "Slide", "slide", "Diagram", "diagram", "Evidence", "evidence", "Note", "note", "Map", "map", "Breaker", "breaker", "Graph", "graph", "Data", "data", "Element", "element", "Lab", "lab", "Instruction", "instruction", "Response", "response", "Question", "question"]
invalidChars = ['~', '#', '%', '&', '*', '{', '}', '\\', ':', '<', '>', '?', '/', '|', '\"', ',']
counter = 0
anchorText = ""
urlToQuote = "https://scioly.org/wiki/index.php/Test_Exchange_Archive"
relativeRootURL = "https://scioly.org"
absoluteDirLoc = ""
linkedURL = ""
fullURL = ""
yearString = ""
yearPattern = re.compile('.*((?<!\S)[1-2][0-9]{3}(?!\S))')
newFileName = ""

def handleError():
	print e.code
	print e.msg
	log.write("Encountered error with link: \"" + linkedURL + "\"")
	log.write("\n Error code: " + str(e.code))
	log.write("\n Error message: " + str(e.msg))
	pass

def writeLog(eventName, yearString, rawAuthor, fullURL):
	parsedAuthor = rawAuthor[:rawAuthor.index(yearString)]+rawAuthor[rawAuthor.index(yearString)+4:]
	if " -- " in parsedAuthor:
		parsedAuthor = parsedAuthor[:parsedAuthor.index(" -- ")]
	parsedAuthor = re.sub("[\(].{25,}[\)]", "", parsedAuthor)
	newFileName = (eventName.replace(" ", "").lower() + "_" + yearString + "_c_" + parsedAuthor.replace(" ", "").replace("-", "") + "_" + anchorText.replace(" ", "") + linkedURL[linkedURL.rfind("."):]).decode('utf-8', 'ignore')
	for i in invalidChars:
		if i in newFileName:
			newFileName = newFileName.replace(i, "")
	log.write("Event: " + eventName)
	log.write("\n Year: " + yearString)
	log.write("\n Link Text: " + anchorText)
	log.write("\n Link: " + linkedURL)
	log.write("\n newFileName: " + newFileName)
	download(fullURL, newFileName)

def download(fullURL, newFileName):
	print "Downloading as: " + newFileName
	targetLocation = absoluteDirLoc + "\\" + newFileName
	print "\n targetLocation: " + targetLocation
	wget.download(fullURL, "raw_data\\" + newFileName) 
	# os.rename(newFileName, ("raw_data\\" + newFileName))
	
def logic():
	if "html" not in str(header):
		# print "File"
		yearString = ""
		hasBeenFound = False
		eventName = anchor.find_previous("h2").get_text()
		print eventName
		if yearPattern.match(anchorText):
			f = yearPattern.match(anchorText).end()
			yearString = anchorText[f-4:f]
			hasBeenFound = True
			print "found match in anchorText"
			print anchorText
			writeLog(eventName, yearString, anchorText, fullURL)
			log.write("\nYYYY match found in anchorText: " + anchorText)
		else:
			gGrandParent = anchor.parent.parent.parent
			gGrandParentText = gGrandParent.get_text().encode('ascii', 'ignore')
			split = gGrandParentText.split("\n")
			if yearPattern.match(split[0]):
				f = yearPattern.match(split[0]).end()
				yearString = split[0][f-4:f]
				hasBeenFound = True
				print "found match in gGrandParentText"
				print split[0]
				writeLog(eventName, yearString, split[0], fullURL)
				log.write("\nYYYY match found in gGrandParentText: " + split[0])
			else:
				greatestGrandParent = gGrandParent.parent.parent
				# print greatestGrandParent
				greatestGrandParentText = greatestGrandParent.get_text().encode('ascii', 'ignore')
				split2 = greatestGrandParentText.split("\n")
				if yearPattern.match(split2[0]):
					f = yearPattern.match(split2[0]).end()
					yearString = split2[0][f-4:f]
					hasBeenFound = True
					print "found match in greatestGrandParentText"
					print split2[0]
					writeLog(eventName, yearString, (split2[0]+"["+split[0]+"]"), fullURL)
					log.write("\nYYYY match found in greatestGrandParent: " + split2[0])
				ggpSib = greatestGrandParent.parent.previous_sibling.previous_sibling
				ggpSibText = ggpSib.get_text().encode('ascii', 'ignore')
				splitGgpSib = ggpSibText.split("\n")
				if yearPattern.match(splitGgpSib[0]) and hasBeenFound is False:
					f = yearPattern.match(splitGgpSib[0]).end()
					yearString = splitGgpSib[0][f-4:f]
					hasBeenFound = True
					print "found match in ggpSib"
					print splitGgpSib[0]
					writeLog(eventName, yearString, splitGgpSib[0], fullURL)
					log.write("\nYYYY match found in ggpSib: " + splitGgpSib[0])
		if not hasBeenFound:
			print "Not Found at any level"
			print anchorText
			print split[0]
			print split2[0]
			print splitGgpSib[0]
			parsedAuthor = split[0]
			parsedAuthor = re.sub("[\(].{25,}[\)]", "", parsedAuthor)
			newFileName = (eventName.replace(" ", "").lower() + "_YYYY_c_" + parsedAuthor.replace(" ", "").replace("-", "") + "_" + anchorText.replace(" ", "") + linkedURL[linkedURL.rfind("."):]).decode('utf-8', 'ignore')
			for i in invalidChars:
				if i in newFileName:
					newFileName = newFileName.replace(i, "")
			log.write("\nYYYY match not found in any level: " + "\n Link: " + linkedURL + "\n Link text: " + anchorText + "\n gGrandParent: " + split[0] + "\n greatestGrandParent: " + split2[0] + "\n ggpSib: " + splitGgpSib[0])
			log.write("\n Generated newFileName: " + newFileName)
			download(fullURL, newFileName)
		# print(str(anchor))
		print(linkedURL)
	else:
		print "Not File"
		log.write("Link: \"" + linkedURL + "\" is not a file. \n Not downloaded")

if ack is "y":
	if not os.path.exists("raw_data"):
		os.makedirs("raw_data")
	# absoluteDirLoc = raw_input("Enter the Absolute file path of the directory in which want unsorted data to be dumped: (i.e. C:\Users\Evan\Desktop\desktop_for_testing): ").decode()
	absoluteDirLoc = "C:\\Users\\Evan\\Desktop\\SciOly\\AHS Scioly Test Stash (2018)\\Testing\\Scraper2\\raw_data"
	pageQuote = urllib2.urlopen(urlToQuote)
	rawHTML = BeautifulSoup(pageQuote, 'html.parser')
	# print rawHTML
	anchors = rawHTML.findAll('a')
	log = open("Scraper2Log.txt","w+")
	for anchor in anchors:
		if any(x in anchor.get_text() for x in triggers):
			log.write("\n \n \n")
			print "\n"
			counter += 1
			anchorText = anchor.get_text().encode('ascii', 'ignore')
			linkedURL = anchor.get('href')
			if "http" in linkedURL:
				# print "Absolute"
				fullURL = linkedURL
				try:
					Response = urllib2.urlopen(linkedURL)
					header = Response.info()
					# print header
					logic()
				except urllib2.HTTPError, e:
					handleError()
			else:
				# print "Relative"
				fullURL = relativeRootURL + linkedURL
				try:
					Response = urllib2.urlopen((relativeRootURL + linkedURL))
					header = Response.info()
					# print header
					logic()
				except urllib2.HTTPError, e:
					handleError()
			# print(anchorText)
	print counter
	log.close()
	exit = raw_input("\n Press any key to exit: ")
else:
	exit = raw_input("\n Press any key to exit: ")