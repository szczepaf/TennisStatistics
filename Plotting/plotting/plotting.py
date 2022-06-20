import json
import urllib.request

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
        if len(line) > 1:
            linesCleared.append(line)

    for line in linesCleared:
        print(line)
        

        ## TODO RETURN 
        ## Special for 2013


def computeMeanForYear(playerArray, dictionary):
    sum = 0
    for player in playerArray:
        sum += dictionary[player]
    mean = sum / 10
    return mean




def main():
    heightsDict = getDict()
    page = getHtml("http://www.tennis28.com/rankings/yearend_topten.html")
    getTopTenForYear(str(1973), page)
    getTopTenForYear(str(2013), page)

    
    


if __name__ == "__main__":
    main()
