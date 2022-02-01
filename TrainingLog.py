"""    
    Learning Objective: reading and writing dictionaries to
    files
    *
    Program Goal: Create a searchable log with lifts performed
    on any given date
    *
    Implementation Checklist
    ✅ take user input into a dictionary (Training Log)
    ✅ write dictionary to file
    ✅ read contents of file
    ✅ organize contents read from file in dictionary
    ❌ perform calculations on items within dictionary
    ✅ search specific dates from training log
    ❌ track personal best in each lift
    ❌ provide progress statistics
"""


import datetime
import re

"""
    Where we access the training log
    -probably not nessecary to use a class
     doing so to learn syntax of classes
    -variables
        -today, Boolean, is most recent log from today?
        -date, String, todays date
        -dailyLog, Dictionary, contains date and lifts
         performed on a single day
        -TrainingLog, Dictionary, Dict of all Dicts read
         from the file (entire training log)
        -prLog, Dictionary, stores all PRs
    -methods
        -__init__, constructor, reads in data from our log file
         and initialized our class variables
        -addSet, adds a lift to our daily log
        -addTonnage, calculates tonnage for 1 lift
        -getLog, returns dailyLog
        -getDate, returns todays date
    -reflections on class
        -class is not nessecary to make this program and overcomplicates the code.
    class TrainingLog:
    #instance variables
    #tonnage = 0
    today = None
    date = None
    dailyLog = {

    }

    trainingLog = {

    }

    prLog = {

    }

    #init def is like a constructor
    def __init__(self):
        self.date = datetime.date.today()
        self.dailyLog['date'] = self.date
        #reading from file horsecockery
        try:
            readInLog(self.dailyLog)
        except:
            print("log.txt does not exist yet")


    #add set
    def addSet(self, lift, weight, reps):
        if lift not in self.dailyLog:
            self.dailyLog[lift] = [weight, reps]
        else:
            self.dailyLog[lift].extend([weight, reps])

    #add tonnage
    def addTonnage(self):
        pass

    #get log
    def getLog(self):
        return self.dailyLog

    #get date
    def getDate(self):
        return self.date
"""
class TrainingLog:
    #instance variables
    #tonnage = 0
    today = None
    date = None
    dailyLog = {

    }

    trainingLog = {

    }

    prLog = {

    }

    #init def is like a constructor
    def __init__(self):
        self.date = datetime.date.today()
        self.dailyLog['date'] = self.date
        #reading from file horsecockery
        try:
            self.trainingLog = readInLog()
            self.checkDate()
            lastEntry = list(self.trainingLog)[-1]
            if self.today:
                for lifts in self.trainingLog[lastEntry]:
                    data = self.trainingLog[lastEntry][lifts].strip("[']")
                    data = data.split("', '")
                    self.dailyLog[lifts] = data
        except:
            print("log.txt does not exist yet")

    #add set
    def addSet(self, lift, weight, reps):
        if lift not in self.dailyLog:
            self.dailyLog[lift] = [weight, reps]
        else:
            self.dailyLog[lift].extend([weight, reps])

    #add tonnage
    def addTonnage(self):
        pass

    #get log
    def getLog(self):
        return self.dailyLog

    #get date
    def getDate(self):
        return self.date

    #sets val for today
    def checkDate(self):
        lastEntry = list(self.trainingLog)[-1]
        year = int(lastEntry[0:4])
        month = int(lastEntry[6:8])
        day = int(lastEntry[10:12])
        check = datetime.date(year, month, day)
        if self.date == check:
            self.today = True
        else:
            self.today = False
    
    #handles writing to file
    def writeOut(self):
        if self.today:
            try:
                file = open("log.txt", 'r+')
                unrefinedLogs = file.read().split('\n')
                file.seek(0)
                del unrefinedLogs[len(unrefinedLogs)-1]
                del unrefinedLogs[len(unrefinedLogs)-1]
                for x in unrefinedLogs:
                    file.write(x)
                    file.write('\n')
                data = str(self.dailyLog)
                file.write(data)
                file.write('\n')
                file.truncate()
                file.close()
                print("overwrote file")

            except:
                print("writeOut fail in today true")

        else:
            try:
                file = open("log.txt", 'a')
                data = str(self.dailyLog)
                file.write(data)
                file.write('\n')
                file.close()
                print("wrote to file")
            except:
                print("writeOut fail in today false")

"""
    this is the def where the whole program runs, our Main()
    -outputs text to console for user to read
    -loop that accepts user input and performs operations on log
"""
def Log():
    quit = False
    print ("Welcome to the training log!")
    log = TrainingLog()

    #loop that runs everything
    while quit != True:

        #takes input for dictionaries
        ans = input("hit A to add set, hit Q to quit: ")
        if (ans == "a"):
            lift = input("Enter Lift: ")
            weight = input("Enter Weight:")
            reps = input("Enter Reps: ")
            log.addSet(lift, weight, reps)
            print(log.getLog())

        #writes our dictionary to file
        else:
            log.writeOut()
            quit = True

#reads dicts in from log
def readInLog():
    trainingLog = {

    }

    try:
        file = open('log.txt', 'r')
        unrefinedLogs = file.read().split('\n')
        file.close()
        del unrefinedLogs[len(unrefinedLogs)-1]
    except:
        print("uh oh spagetti-o")
    print(len(unrefinedLogs))
    
    for x in unrefinedLogs:
        vals = parse(x)
        trainingLog[vals[0]] = vals[1]
    
    print(trainingLog)
    print()
    return trainingLog


"""
    Goal: parse string into keys and values for dictionary

    Specific demands of our parser
    -remove brackets{} from either side of the dict
    -'date': datetime.date(YYYY, MM, DD)   first item
        -35 char long always at the start
        -key 'date'
        -value 'YYYY, MM, DD'
        -value will become key for days dictionary in the super log
    -'lift': [weight, reps, weight, reps... pattern continues as long as needed]
        -key 'lift'
        -value [list of sets]
    -Main issue
        -list, date, and key:value pairs are separated by \,
        -must determine another way of spliting key:value pairs

    -example string (in order of modification)
        -{'date': datetime.date(2021, 12, 16), 'bench': ['135', '10', '225', '5'], 'squat': ['315', '1']}
        -'date': datetime.date(2021, 12, 16), 'bench': ['135', '10', '225', '5'], 'squat': ['315', '1']
        -'bench': ['135', '10', '225', '5'], 'squat': ['315', '1']
"""
def parse(string):
    #our return vals as a list (date, dict of key:vals)
    returnList = []
    innerDict = {

    }

    #this chunk trims the string and fetches our date
    string = string.strip('{}')
    date = string[22:34]
    returnList.append(date)
    string = string[37:]

    #this chunk deals with separating our lifts and sets
    #inserts an extra ] char at all delimited indicies
    indiciesObject = re.finditer(pattern='], ', string=string)
    indicies = [index.start() for index in indiciesObject]
    indexIncriment = 0
    for x in range(len(indicies)):
        indicies[x] = indicies[x] + indexIncriment
        indexIncriment+=1
    for index in indicies:
        string = string[:index] + ']' + string[index:]
    pairs = string.split('], ')

    #trying to make build innerDict from pairs
    for x in pairs:
        pair = x.split(': ')
        innerDict[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    returnList.append(innerDict)

    #deals with returning the data we need to work with
    return returnList


#call to our main function, needed to run the program
Log()