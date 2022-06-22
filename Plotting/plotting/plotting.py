import json
from os import linesep
import urllib.request
import matplotlib.pyplot as plt

y2014 = ["Novak Djokovic", "Roger Federer", "Rafael Nadal", "Stan Wawrinka", "Kei Nishikori", "Andy Murray", "Tomas Berdych", "Milos Raonic", "Marin Cilic", "David Ferrer"]
y2015 = ["Novak Djokovic", "Andy Murray", "Roger Federer", "Stan Wawrinka", "Rafael Nadal", "Tomas Berdych", "David Ferrer", "Kei Nishikori", "Richard Gasquets", "Jo-Wilfried Tsonga"]
y2016 = ["Andy Murray", "Novak Djokovic", "Milos Raonic", "Stan Wawrinka", "Kei Nishikori", "Marin Cilic", "Gael Monfils", "Dominic Thiem", "Rafael Nadal", "Tomas Berdych"]
y2017 = ["Rafael Nadal", "Roger Federer", "Grigor Dimitrov", "Alexander Zverev", "Dominic Thiem", "Marin Cilic", "David Goffin", "Jack Sock", "Stan Wawrinka", "Pablo Carreno Busta"]
y2018 = ["Novak Djokovic", "Rafael Nadal", "Roger Federer", "Alexander Zverev", "Juan Martin del Potro", "Kevin Anderson", "Marin Cilic", "Dominic Thiem", "Kei Nishikori", "John Isner"]
y2019 = ["Rafael Nadal","Novak Djokovic", "Roger Federer", "Dominic Thiem","Daniil Medvedev","Stefanos Tsitsipas", "Alexander Zverev", "Matteo Berrettini","Roberto Bautista Agut","Gael Monfils"]
y2020 = ["Novak Djokovic", "Rafael Nadal","Dominic Thiem","Daniil Medvedev","Roger Federer","Stefanos Tsitsipas", "Alexander Zverev","Andrey Rublev","Diego Schwartzmann","Matteo Berrettini"]
y2021 = ["Novak Djokovic","Daniil Medvedev","Alexander Zverev","Stefanos Tsitsipas","Andrey Rublev","Rafael Nadal","Matteo Berrettini","Casper Ruud","Hubert Hurkacz","Janik Sinner"]

def getHtml(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    page = mybytes.decode("utf8")
    fp.close()
    return page


def getDict():
    f = open("heights_corrected.json")  
    heightsDict = json.load(f)
    f.close()

    return heightsDict

def getTopTenForYear(year, page):
    separator = year + "\n</th></tr>"
    years = (page.split(separator)[1]).split("</table>")[0]
    lines = years.split("\n")
    linesCleared = []


    for line in lines:
        if len(line) > 12: #cause of some special lines in the html code
            linesCleared.append(line)
    
    linesParsed = []
    for line in linesCleared:
        lineParsed = parseLine(line)
        #print(lineParsed)
        linesParsed.append(lineParsed)

        
    return linesParsed
       

def parseLine(line):
    #example:
    #<tr><td width = 25% align=center>1</td><td align=left>Ilie Nastase</td></tr>
    return (line.split("<td align=left>")[1]).split("</td></tr>")[0]

def computeMeanForYear(playerArray, dictionary):
    sum = 0
    for player in playerArray:
        sum += float(dictionary[player])
    mean = sum / 10

    return round(mean,3)


def computeMeans(metaList, dictionary):
    means = []
    for yearList in metaList:
        means.append(computeMeanForYear(yearList, dictionary))

    return means


def main():
    heightsDict = getDict()
    page = getHtml("http://www.tennis28.com/rankings/yearend_topten.html")

    listWithPlayerLists = []

    for i in range(1973,2014):
        yearList = getTopTenForYear(str(i),page)
        listWithPlayerLists.append(yearList)


    listWithPlayerLists.append(y2014)
    listWithPlayerLists.append(y2015)
    listWithPlayerLists.append(y2016)
    listWithPlayerLists.append(y2017)
    listWithPlayerLists.append(y2018)
    listWithPlayerLists.append(y2019)
    listWithPlayerLists.append(y2020)
    listWithPlayerLists.append(y2021)

    means = computeMeans(listWithPlayerLists, heightsDict)

    


    years = []
    for i in range(1973, 2022):
        years.append(i)



    plt.scatter(years, means, c = "blue")
    plt.show()

    


    
    


if __name__ == "__main__":
    main()
