import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage,AnnotationBbox
import datetime

flagDir = "/home/country-flag-icons/images/png/"
name_convert = {"Spain":"esp", "Germany":"deu", "China":"chn",'USA':'usa','Italy':'ita','United Kingdom':'gbr',
                'Austria':'aus','Slovakia':'svk','Singapore':'sgp','Indonesia':'idn','Vietnam':'vnm','Thailand':'tha',
                'Malaysia':'mys','Netherlands':'nld','Russia':'rus','Sweden':'swe',"Denmark":'dnk','Czechia':'cze',
                'EU':'eu','Belarus':'blr','Canada':'can','Korea':'kor','Brazil':'bra','Taiwan':'twn','Iran':'irn','Hong Kong':'hkg',
                'Japan':'jpn','Ukraine':'ukr','Switzerland':'che'}

def get_flag(name):
    path = flagDir+name_convert[name]+".png"
    im = plt.imread(path)
    return im

def offset_image(coord, name, ax):
    img = get_flag(name)
    factor = 1/(img.shape[0]/30.0)
    im = OffsetImage(img, zoom=factor)
    im.image.axes = ax

    ab = AnnotationBbox(im, (coord, 0),  xybox=(0., -20.), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)

countries = ["China", "Russia", "EU", "USA",'Belarus','Canada','Korea','United Kingdom']#,'Brazil','Taiwan','Singapore','Iran','Hong Kong','Japan','Ukraine','Switzerland','Vietnam']
valuesA = [9, 8, 7,7,2,2,2,2]#,1,1,1,1,1,1,1,1,1]

fig, ax = plt.subplots()

ax.bar(range(len(countries)), valuesA, width=0.5,align="center")
ax.set_xticks(range(len(countries)))
ax.set_xticklabels(countries,fontsize=16)
ax.tick_params(axis='x', which='major', pad=36)


for i, c in enumerate(countries):
    offset_image(i, c, ax)

plt.xlabel('Countries', fontsize=18)
plt.ylabel('Number of universities in top50', fontsize=18)
plt.title('Countries by number of top universities at ACM ICPC', fontsize=24)
plt.show()

fig.savefig('worlds.png', format='png',bbox_inches='tight',dpi=600)
