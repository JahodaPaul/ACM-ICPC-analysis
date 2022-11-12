import math
import sys
from datetime import date
from utils import *
import argparse

def argument_parser():
  # helps parsing the same arguments in a different script
  parser = argparse.ArgumentParser()
  parser.add_argument('--region', default='finals', choices=['finals', 'nwerc', 'cerc','napnw','swerc','nane'])
  parser.add_argument('--verbose', default='False', choices=['True', 'False'])
  
  return parser
  
            
def CalculatePointsPerInstitution(table,overall, factor=1,printTop3=True):
    thisYearInst = {}
     
    for item in table:
        institution = item[0]
        place = item[1]
        points = math.pow((len(table)-int(place)+1)/float(len(table)),2)
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
        if item[1] not in overall.keys():
            overall[item[1]] = item[0]*factor
        else:
            overall[item[1]] += item[0] * factor


def CalculatePointsPerCountry(table,overall, factor=1, printTop3=True):
    thisYearCountry = {}

    for item in table:
        institution = item[0]
        place = item[1]
        
        if institution in insitution_to_country.keys():
       	    points = math.pow((len(table)-int(place)+1)/float(len(table)),2)
            country = insitution_to_country[institution]
            if country not in thisYearCountry.keys():
            	thisYearCountry[country] = [points,1]
            else:
            	thisYearCountry[country][0] += points
            	thisYearCountry[country][1] += 1

        
    arrCountries = []
    for key in thisYearCountry.keys():
        arrCountries.append([thisYearCountry[key][0]/float(math.sqrt(thisYearCountry[key][1])),key])
    
    
    arrCountries.sort(reverse=True)
    if printTop3:
        for i in range(3):
            print(str(i+1)+'.',arrCountries[i][1],'   points:',arrCountries[i][0])
        print()
            
    for item in arrCountries:
        if item[1] not in overall.keys():
    	    overall[item[1]] = item[0]*factor
        else:
            overall[item[1]] += item[0] * factor

def Run(region,verbose):
    # institution, points
    overallPoints = {}
    overallPointsCountry = {}
    year = int(date.today().year)
    if True:
        for i in range(0, 10):
            id = getID(region, year-11 + i)
            table = getTable(id)
            CalculatePointsPerInstitution(table, overallPoints, (i + 1) / 10.0)
            if verbose=='True':
                CalculatePointsPerCountry(table, overallPointsCountry, (i + 1) / 10.0)
            else:
                CalculatePointsPerCountry(table, overallPointsCountry, (i + 1) / 10.0,False)

        # Final print
        arr = []
        for key in overallPoints.keys():
            arr.append([overallPoints[key], key])
        arr.sort(reverse=True)

        print('Overall:')
        for i in range(len(arr)):
            if i>=100 and verbose=='False':
                continue
            print(str(i + 1) + '.', arr[i][1], '   points:', arr[i][0])
            
        arrCountries = []
        for key in overallPointsCountry.keys():
            arrCountries.append([overallPointsCountry[key], key])
        arrCountries.sort(reverse=True)
        
        print()
       	print('Overall Countries:')
        for i in range(len(arrCountries)):
            print(str(i + 1) + '.', arrCountries[i][1], '   points:', arrCountries[i][0])
          
    #except Exception as ex:
    #    print(ex)


if len(sys.argv) == 2:
    parser = argument_parser()
    args = parser.parse_args()
    Run(args.region,args.verbose)



