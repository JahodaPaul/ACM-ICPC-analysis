import json
import urllib.request


region_abbr_to_linkname = {'cerc':'central-europe','nwerc':'northwestern-europe','finals':'World-Finals','swerc':'swerc','nane':'northeast-north-america','napnw':'Pacific-Northwest'}

insitution_to_country = {'St. Petersburg ITMO University':'Russia','University of Warsaw':'Poland','Moscow State University':'Russia',
			'Massachusetts Institute of Technology':'USA','National Taiwan University':'Taiwan','Moscow Institute of Physics and Technology':'Russia',
			'The University of Tokyo':'Japan','Shanghai Jiao Tong University':'China','St. Petersburg State University':'Russia',
			'Tsinghua University':'China', 'Peking University':'China','University of Wroclaw':'Poland',
			'Fudan University':'China', 'Belarusian State University':'Belarus','Seoul National University':'South Korea',
			'University of Central Florida':'USA', 'Harvard University':'USA','Sharif University of Technology':'Iran',
			'Saratov State University':'Russia','Ural Federal University':'Russia','Jagiellonian University in Krakow':'Poland',
			'National Research University Higher School of Economics':'Russia','KAIST':'South Korea','University of Bucharest':'Romania',
			'ETH Zürich':'Switzerland','Stanford University':'USA','Beihang University':'China',
			'Canada':'University of Waterloo','Zhongshan (Sun Yat-sen) University':'China','The Chinese University of Hong Kong':'Hong Kong',
			'University of Zagreb':'Croatia'}
			
countries_to_regions = {'Poland':'EU','Romania':'EU','Croatia':'EU'}



def getID(contestName,year):
    contestName = region_abbr_to_linkname[contestName]
    print(contestName, str(year))
    url = "https://icpc.global/api/contest/public/"+ contestName + '-' + str(year)
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    res = json.loads(mystr)
    return str(res['id'])

def getTable(contestID):
    url = "https://icpc.global/api/contest/public/search/contest/"+str(contestID)+\
          "?q=proj:rank,institution,teamName,problemsSolved,totalTime,lastProblemTime,medalCitation;sort:rank%20asc,problemsSolved%20desc,totalTime%20asc,lastProblemTime%20asc;&page=1&size=1000"
          
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    res = json.loads(mystr)
    
    # institution, place
    table = []

    counter = 0
    for item in res:
        counter += 1
        place = counter
        institution = item['institution']
        table.append([institution,place])
        
    return table
