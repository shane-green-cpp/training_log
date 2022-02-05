import re
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

    print(trainingLog['2021, 12, 17']['bench'])


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

readInLog()