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
			'University of Waterloo':'Canada','Zhongshan (Sun Yat-sen) University':'China','The Chinese University of Hong Kong':'Hong Kong',
			'University of Zagreb':'Croatia','Lviv National University':'Ukraine','University of Cambridge':'United Kingdom',
'Nizhny Novgorod State University':'Russia',
			'UNSW Sydney':'Australia','University of Helsinki':'Finland',
                                                               'Zhejiang University': 'China',
                                                                                        'National University of Singapore': 'Singapore',
'University of Electronic Science and Technology of China': 'China',
'University of California, Berkeley': 'USA',
'Carnegie Mellon University': 'USA',
'Taras Shevchenko National University of Kyiv': 'Ukraine',
'University of Engineering and Technology - VNU': 'Vietnam',
'Belarusian State University of Informatics and Radioelectronics': 'Belarus',
'Universidad de Buenos Aires - FCEN': 'Brazil',
'St. Petersburg Academic University': 'Russia',
'Korea University': 'South Korea',
'The University of British Columbia': 'Canada',
'University of Latvia': 'Latvia',
'University of Southern California': 'USA',
'Perm State University': 'Russia',
'Fuzhou University': 'China',
'Universidad Nacional de Córdoba - FaMAF': 'Argentina',
'Kyoto University': 'Japan',
'Universidade Federal de Pernambuco': 'Brazil',
'Universitas Indonesia': 'Indonesia',
'University of Illinois at Urbana-Champaign': 'USA',
'Universitat Politècnica de Catalunya': 'Spain',
'Bangladesh University of Engineering and Technology': 'Bangladesh',
'Universidade de São Paulo': 'Brazil',
'Novosibirsk State University': 'Russia',
'University of Wisconsin-Madison': 'USA',
'International Institute of Information Technology - Hyderabad': 'India',
'Moscow Aviation Institute': 'Russia',
'Beijing Normal University': 'China',
'South China University of Technology': 'China',
'Hangzhou Dianzi University': 'China',
'University of Oxford': 'United Kingdom',
'Vilnius University': 'Lithuania',
'Indian Institute of Technology - Bombay': 'India',
'École Normale Supérieure de Paris': 'France',
'Charles University in Prague': 'Czechia',
'Indian Institute of Technology - Roorkee': 'India',
'Indian Institute of Technology - Delhi': 'India',
'KTH - Royal Institute of Technology': 'Sweden',
'Universidad Nacional de Rosario': 'Argentina',
'Scuola Normale Superiore': 'Italy',
'National Yang Ming Chiao Tung University': 'Taiwan',
'University of Tsukuba': 'Japan',
'Indian Institute of Technology - Kanpur': 'India',
'University of Michigan at Ann Arbor': 'USA',
'Technische Universität München': 'Germany',
'Kharkiv National University of Radio Electronics': 'Ukraine',
'Cornell University': 'USA',
'The University of Texas at Austin': 'USA',
'Beijing University of Posts and Telecommunications': 'China',
'Institut Teknologi Bandung': 'Indonesia',
'St. Petersburg Campus of Higher School of Economics': 'Russia',
'Tokyo Institute of Technology': 'Japan',
'University of Aizu': 'Japan',
'Shanghai University': 'China',
'Universidade de São Paulo - Campus de São Carlos': 'Brazil',
'Innopolis University': 'Russia',
'Comenius University': 'Slovakia',
'International IT University': 'Kazakhstan',
'Columbia University': 'USA',
}
			
countries_to_regions_EU = {'Poland':'EU','Romania':'EU','Croatia':'EU','Finland':'EU','Latvia':'EU','Spain':'EU','Lithuania':'EU','France':'EU','Czechia':'EU',
                            'Sweden':'EU','Italy':'EU','Germany':'EU','Slovakia':'EU'}

countries_to_regions_whole = {'Poland':'Europe','Romania':'Europe','Croatia':'Europe','Finland':'Europe','Russia':'Russia','China':'Asia','South Korea':'Asia','Japan':'Asia','Belarus':'Europe','USA':'North America',
			      'Australia':'Asia','Canada':'North America','United Kingdom':'Europe','Switzerland':'Europe','Taiwan':'Asia','Hong Kong':'Asia','Iran':'Asia','Ukraine':'Europe','Singapore':'Asia',
                              'Vietnam':'Asia','Brazil':'South America','Latvia':'Europe','Spain':'Europe','Indonesia':'Asia','Argentina':'South America','Bangladesh':'Asia','India':'Asia'
                              ,'Lithuania':'Europe','France':'Europe','Czechia':'Europe','Sweden':'Europe','Italy':'Europe','Germany':'Europe','Slovakia':'Europe','Kazakhstan':'Asia'}



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
        problemSolved = item['problemsSolved']
        if problemSolved==None:
           problemSolved = 1.0
        table.append([institution,place,problemSolved])
        
    return table

def PrintUniRankings(rankings, verbose):
    arr = []
    for key in rankings.keys():
        arr.append([rankings[key], key])
    arr.sort(reverse=True)

    print('Overall:')
    for i in range(len(arr)):
        if i >= 100 and verbose == 'False':
            continue
        print(str(i + 1) + '.', arr[i][1], '   points:', arr[i][0])
        # print('\'',arr[i][1], '\':', '\'\',')


def PrintCountryRankings(rankings, verbose):
    arrCountries = []
    for key in rankings.keys():
        arrCountries.append([rankings[key], key])
    arrCountries.sort(reverse=True)

    print()
    print('Overall Countries:')


    for i in range(len(arrCountries)):
        print(str(i + 1) + '.', arrCountries[i][1], '   points:', arrCountries[i][0])


def PrintRegionRankings(rankings, verbose):
    arrRegions = []
    for key in rankings.keys():
        arrRegions.append([rankings[key], key])
    arrRegions.sort(reverse=True)

    print()
    print('Overall Regions:')


    for i in range(len(arrRegions)):
        print(str(i + 1) + '.', arrRegions[i][1], '   points:', arrRegions[i][0])

def PrintUniInRegionrRanking(rankings, regionName, verbose):
    arr = []
    for key in rankings.keys():
        arr.append([rankings[key], key])
    arr.sort(reverse=True)

    if regionName == 'EU':
        print('Overall ',regionName,':')
        counter = 0
        for i in range(len(arr)):
            if arr[i][1] in insitution_to_country.keys():
                country = insitution_to_country[arr[i][1]]
                if country in countries_to_regions_EU.keys():
                    print(str(counter + 1) + '.', arr[i][1], '   points:', arr[i][0])
                    counter += 1
    else:
        print('Overall ',regionName,':')
        counter = 0
        for i in range(len(arr)):
            if arr[i][1] in insitution_to_country.keys():
                country = insitution_to_country[arr[i][1]]
                if countries_to_regions_whole[country] == regionName:
                    print(str(counter + 1) + '.', arr[i][1], '   points:', arr[i][0])
                    counter += 1