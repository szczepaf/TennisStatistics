import urllib.request
import urllib.parse
import json


#The database I used covered only the years 1973 - 2013, so I created manually the last few years

y2014 = ["Novak Djokovic", "Roger Federer", "Rafael Nadal", "Stan Wawrinka", "Kei Nishikori", "Andy Murray", "Tomas Berdych", "Milos Raonic", "Marin Cilic", "David Ferrer"]
y2015 = ["Novak Djokovic", "Andy Murray", "Roger Federer", "Stan Wawrinka", "Rafael Nadal", "Tomas Berdych", "David Ferrer", "Kei Nishikori", "Richard Gasquets", "Jo-Wilfried Tsonga"]
y2016 = ["Andy Murray", "Novak Djokovic", "Milos Raonic", "Stan Warinka", "Kei Nishikori", "Marin Cilic", "Gael Monfils", "Dominic Thiem", "Rafael Nadal", "Tomas Berdych"]
y2017 = ["Rafael Nadal", "Roger Federer", "Grigor Dimitrov", "Alexander Zverev", "Dominic Thiem", "Marin Cilic", "David Goffin", "Jack Sock", "Stan Wawrinka", "Pablo Carreno Busta"]
y2018 = ["Novak Djokovic", "Rafael Nadal", "Roger Federer", "Alexander Zverev", "Juan Martin del Potro", "Kevin Anderson", "Marin Cilic", "Dominic Thiem", "Kei Nishikori", "John Isner"]
y2019 = ["Rafael Nadal","Novak Djokovic", "Roger Federer", "Dominic Thiem","Daniil Medvedev","Stefanos Tsitsipas", "Alexander Zverev", "Matteo Berrettini","Roberto Bautista Agut","Gael Monfils"]
y2020 = ["Novak Djokovic", "Rafael Nadal","Dominic Thiem","Daniil Medvedev","Roger Federer","Stefanos Tsitsipas", "Alexander Zverev","Andrey Rublev","Diego Schawrtzmann","Matteo Berrettini"] 
y2021 = ["Novak Djokovic","Daniil Medvedev","Alexander Zverev","Stefanos Tsitsipas","Andrey Rublev","Rafael Nadal","Matteo Berrettini","Casper Ruud","Hubert Hurkacz","Janik Sinner"]


def getHtml(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def getNamesFromString(html):
    lines = html.splitlines()
    names = []
    for line in lines:
        
        if line.startswith("<tr><td"):
            name = (line.split("left>")[1]).split("</td>")[0]
            names.append(name)
    return names

def getHeightByName(name):
    url = 'http://start.csail.mit.edu/justanswer.php'

    #Answering machine from MIT might seem like a little funny choice for retrieving the heights,
    #but no tennis database I found offered a clear overview of top players with their heights

    query = 'How tall is ' + name + '?'
    values = { 'query': query }

    data = urllib.parse.urlencode(values)
    url = '?'.join([url, data])
    response = urllib.request.urlopen(url)

    pageBytes = response.read()
    pageString = pageBytes.decode('UTF-8')

    try:
        if "Height</span>:" in pageString:
            height = (pageString.split("Height</span>: ")[1]).split(" ", 1)[0]
        else:
            height = (pageString.split("Height: ")[1]).split(" ", 1)[0]
        if len(height) == 1:
            #In case the height in in feet and not cm
            pattern = " m)"
            height = (pageString.split("in (")[1]).split(pattern)[0]
    except Exception:
        height = "bad formatting"

    print(name, height)
    return height


def getNames1973_2013():
    html = getHtml("http://www.tennis28.com/rankings/yearend_topten.html")
    allNames = getNamesFromString(html)
    names = []
    [names.append(x) for x in allNames if x not in names] 
    return names

#Final function for storing the dictionary with names:heights - call this in main
def createDict():
    namesTwoAll = y2014 + y2015 + y2016 + y2017 + y2018 + y2019 + y2020 + y2021
    namesTwo = []
    [namesTwo.append(x) for x in namesTwoAll if x not in namesTwo] #filtered names

    heightDictionary = dict()

    namesOne = getNames1973_2013()
    namesFinal = namesOne + namesTwo #complete filtered list of names 

    for name in namesFinal:

        heightDictionary[name] = getHeightByName(name)
    

    f = open("heights.json", "w") #this will still have some mistakes, need to correct a few entries manually
    json.dump(heightDictionary, f)
    f.close()


def main():
    createDict()

    
if __name__ == "__main__":
    main()

