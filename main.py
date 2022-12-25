import math
import sys
from datetime import date
from utils import *
import argparse
import os

def argument_parser():
  # helps parsing the same arguments in a different script
  parser = argparse.ArgumentParser()
  parser.add_argument('--region', default='finals', choices=['finals', 'nwerc', 'cerc','napnw','swerc','nane'])
  parser.add_argument('--verbose', default='False', choices=['True', 'False'])
  
  return parser
  
  
def PointsCalculation(n_of_teams, place, maxProblemsSolved, problemsSolved):
    points = math.pow((n_of_teams-place+1)/float(n_of_teams) * (problemsSolved/maxProblemsSolved),1)
    return points
  
            
def CalculatePointsPerInstitution(table,overall, factor=1,printTop3=True):
    thisYearInst = {}
    
    maxProblemSolved = -1
     
    for item in table:
        institution = item[0]
        place = item[1]
        if maxProblemSolved == -1:
            maxProblemSolved = item[2]
        
        points = PointsCalculation(len(table),float(place),float(maxProblemSolved),float(item[2]))
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
    
    maxProblemSolved = -1

    for item in table:
        institution = item[0]
        place = item[1]
        if maxProblemSolved == -1:
            maxProblemSolved = item[2]

        
        if institution in insitution_to_country.keys():
       	    points = PointsCalculation(len(table),float(place),float(maxProblemSolved),float(item[2]))
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
            
def CalculatePointsPerRegion(table,overall, factor=1, printTop3=True):
    thisYearCountry = {}
    
    maxProblemSolved = -1

    for item in table:
        institution = item[0]
        place = item[1]
        if maxProblemSolved == -1:
            maxProblemSolved = item[2]

        
        if institution in insitution_to_country.keys():
       	    points = PointsCalculation(len(table),float(place),float(maxProblemSolved),float(item[2]))
            country = insitution_to_country[institution]
            if country in countries_to_regions_EU.keys():
                country = countries_to_regions_EU[country]
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
    overallPointsRegion = {}
    year = int(date.today().year)
    
    if not os.path.exists('data'):
        os.mkdir('data')
        
    for i in range(0, 10):
        try:
            current_year = year-10 + i
            path = 'data/' + region + '_' + str(current_year) +'.txt'
            if not os.path.exists(path):
                id = getID(region, current_year)
                table = getTable(id)
                saveData(table,path)
            else:
                table = loadData(path)
            if len(table) == 0:
                continue
            CalculatePointsPerInstitution(table, overallPoints, (i + 1) / 10.0)
            if verbose=='True':
                CalculatePointsPerCountry(table, overallPointsCountry, (i + 1) / 10.0)
            else:
                CalculatePointsPerCountry(table, overallPointsCountry, (i + 1) / 10.0,False)
                
            if verbose=='True':
                CalculatePointsPerRegion(table, overallPointsRegion, (i + 1) / 10.0)
            else:
                CalculatePointsPerRegion(table, overallPointsRegion, (i + 1) / 10.0,False)
        except Exception as ex:
            print(ex)

    # Final print
    PrintUniRankings(overallPoints,verbose)
    PrintCountryRankings(overallPointsCountry,verbose)
    PrintRegionRankings(overallPointsRegion, verbose)
    PrintUniInRegionrRanking(overallPoints,'EU',verbose)
          



parser = argument_parser()
args = parser.parse_args()
Run(args.region,args.verbose)



