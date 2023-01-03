import urllib.request
import sys
import time

#returns the string contents of the page at url, or "" if there is an error
def read_url(url):
	fail_count = 0
	
	while fail_count < 10:
		#time.sleep(1)
		try:
			fp = urllib.request.urlopen(url)
			mybytes = fp.read()

			mystr = mybytes.decode(sys.stdout.encoding)
			fp.close()
			#mystr = mystr.split("\n")
			return mystr
		except:
			fail_count += 1
			print("Failed to read " + url + "(" + str(fail_count) + ")")
	return ""
def crawl():
    theHTML = read_url("https://oirp.carleton.ca/databook/2021/courses/tables/table-CE1-1_hpt.htm")
    aList = []
    firstYearCourses = ""
    line = ""
    for line in theHTML.split("\n"):
        for aPart in line.split(";"):
            aPart = aPart.replace("BR","")
            aPart = aPart.replace("<#e8e8e8>",",")
            aPart = getRidOfSemantics(aPart)
            aPart = aPart.strip()
            if((aPart.find("(")==0 and aPart.find(")")==5) or "Faculty Total" in aPart):
                aPart = aPart.replace(",","")
                firstYearCourses += aPart+","

        if(line.endswith("</NOBR></TD>")):
            line = line.replace(";","")
            line = line.replace("BR",",")
            line = getRidOfSemantics(line)
            if(line.endswith("NO,")):
                line = line.replace("NO,","")
                if(line[0:1]==','):
                    line = line[1:len(line)-1]
                if(line[len(line)-1:len(line)]==","):
                    line = line[:len(line)-2]
                aList.append(line)

    #make a variable to do keep track
    isCourses = False
    intWait = 7
    firstYearNumbersLine = ""

    for i in range(0,len(aList)):
        isCourses = checkIfCourses(aList[i],isCourses)

        #if it's the course, then wait
        if(isCourses == True):
            intWait-=1
        
        if(intWait==0):
            firstYearNumbersLine += aList[i]+","
            isCourses = False
            intWait=7

    courseEnrolmentDictionary = {}
    firstYearCoursesArray = firstYearCourses.split(",")
    firstYearNumbersArray = firstYearNumbersLine.split(",")

    for i in range(0,len(firstYearCoursesArray)):
        courseEnrolmentDictionary[firstYearCoursesArray[i]] = firstYearNumbersArray[i]
    return sortt(courseEnrolmentDictionary)
    
    

def checkIfCourses(line,isCourses):
    char1 = line[0:1]
    # if the first isn't a digit and it's not a comma, then print it
    if(not char1.isnumeric() and not char1 ==","):
        return True
    return isCourses

def getRidOfSemantics(line):
    line = line.replace("&nbsp","")
    line = line.replace("NOBR","")
    line = line.replace("TD","")
    line = line.replace("<","") 
    line = line.replace(">","") 
    line = line.replace("/","") 
    line = line.replace("Strong","") 
    return line

def sortt(dictionary):
    print("sorting")
    aList = []
    for key,value in dictionary.items():
        aList.append([key,value])

    i=0
    while i < len(aList):
        if "Faculty" in aList[i][0] or aList[i][1]=="":
            aList.pop(i)
            i-=1
        i+=1

    for i in range(len(aList)):
        for x in range(len(aList)-2):
            if int(aList[x][1]) < int(aList[x+1][1]):
                temp = aList[x]
                aList[x]=aList[x+1]
                aList[x+1]=temp
    return aList

if __name__ == "__main__":
    crawl()