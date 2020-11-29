import urllib.request
import json
import math
import sys

# institution, points
overallPoints = {}

def getID(contestName,year):
    print(contestName, str(year))
    url = "https://icpc.global/cm5-contest-rest/rest/contest/public/"+ contestName + '-' + str(year)
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    res = json.loads(mystr)
    return str(res['id'])

def getTable(contestID, factor, printTop3=True):
    url = "https://icpc.global/cm5-contest-rest/rest/contest/standings/contest/"+str(contestID)+\
          "?q=proj:place,institution,team,problemsSolved,totalTime,lastSolution;sort:place%20asc;&page=1&size=1000"
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    res = json.loads(mystr)
    thisYearInst = {}

    counter = 0
    for item in res:
        counter += 1
        place = counter
        institution = item['institution']
        points = math.pow(len(res)-int(place),2)
        if institution not in thisYearInst.keys():
            thisYearInst[institution] = [points,1]
        else:
            thisYearInst[institution][0] += points
            thisYearInst[institution][1] += 1

    arr = []
    for key in thisYearInst.keys():
        arr.append([thisYearInst[key][0]/float(math.sqrt(thisYearInst[key][1])),key])
    arr.sort(reverse=True)
    if printTop3:
        for i in range(3):
            print(str(i+1)+'.',arr[i][1],'   points:',arr[i][0])
        print()

    for item in arr:
        if item[1] not in overallPoints.keys():
            overallPoints[item[1]] = item[0]*factor
        else:
            overallPoints[item[1]] += item[0] * factor

def Run(region):
    try:
        for i in range(0, 10):
            id = getID(region, 2010 + i)
            getTable(id, (i + 1) / 10.0)

        # Final print
        arr = []
        for key in overallPoints.keys():
            arr.append([overallPoints[key], key])
        arr.sort(reverse=True)

        print('Overall:')
        for i in range(len(arr)):
            print(str(i + 1) + '.', arr[i][1], '   points:', arr[i][0])
    except Exception as ex:
        print(ex)
        print('The program takes one argument - the name of the region (such as northwestern-europe) ')
    # tested name of the regions :
    # northwestern-europe
    # central-europe
    # Pacific-Northwest
    # World-Finals
    # swerc
    # northeast-north-america

if len(sys.argv) == 2:
    Run(sys.argv[1])



