# Průměrná výška nejlepších tenistů v čase

### Statistická práce pro předmět Pravděpodobnost a Statistika 1, 2022, MFF UK, František Szczepanik

#### Úvod
Tenis se v posledních několika posledních dekádách velmi zřetelně profesionalizoval - stejně jako to ostatně proběhlo u celé řady dalších sportovních disciplín. Nedošlo jen k posunu v oblasti technologií (zejména výrobě raket), ale i v herním stylu.  

Řada komentátorských nestorů a tenisových legend (někdy s lítostí) prosazuje názor, že dominantím způsobem hry se stal styl, kdy hráč zůstává na základní čáře a silnými údery diktuje podobu výměny (offensive baselining), narozdíl například od kreativnější hry u sítě či chytře umístěných krátkých drop-shotů. S tím se údajně  pojí rostoucí průměrná výška nejlepších hráčů a fenomén servebotingu - tedy typu vysokého hráče, který má extrémně silné podání, ale v ostatních aspektech jeho hra pokulhává a je spíše nudná a nekreativní.

V této práci tedy prozkoumám, zdali opravdu výška nejlepších hráčů roste. Pro roky 1973 - 2021 spočítám průměrnou výšku deseti nejlepších hráčů daného roku a lineární regresí zjistím, jestli tento průměr roste v čase.

#### Postup
Do hashsetu jsem uložil všechny hráče, kteří se od roku 1973 objevili v top desítce rankingu, spočítal jsem jejich výšku a pak pro každý rok spočítal průměr daných top deseti hráčů.

Žádná tenisová databáze však nenabízela uspořádaná data o top 10 hráčích na konci daného roku, žádná tenisová databáze také nenabízela uspořádaná data ve formátu hráč:jeho výška. Proto jsem data scrapoval z různých webů, například z http://www.tennis28.com/rankings/yearend_topten.html. Pro pár posledních let data chyběla a tak jsem musel databázi hráčů dokončit manuálně.

Následně jsem pomocí answering machine MIT (a patřičného parsování) získal potřebné výšky hráčů, uložil je do slovníku (v podobě hráč:výška), opravil ručně několik chyb vzniklých odlišností html kódu pro stránku s odpovědí na výšku daného hráče (soubor heights_corrected.json), pro každý rok naparsoval z výše uvedeného webu top 10 hráčů, spočítal průměry a pomocí python knihoven numpy, sklearn a matplotlib provedl lineární regresi a její visualizaci. Další použitá python knihovna je urllib - pro získávání dat z webu.

Oba python programy (pro scrapování dat - CreatingDict.py - a pak pro spočítání regrese - plotting.py) jsou v repozitáři https://github.com/szczepaf/TennisStatistics.

#### Výsledky Regrese
Takto vypadá ScatterPlot s roky na x-axis a průměrnými výškami na y-axis:
![scatter](https://user-images.githubusercontent.com/83585883/175540671-551afe70-4bd7-4aa4-8185-0e4db9be8605.png)


Na první pohled je zřetelné, že opravdu dochází k růstu, a to ve dvou vlnách - první je v osmdesetých letech, pak nastal mírný pokles, od roku 2005 do 2020 však hodnoty narostly podstatně výše až k 1.9 metrům.  
Období růstu 2005 až do současnosti koresponduje s dvacetiletou dominancí poměrně vysoké Big Three (Nadal, Federer, Djokovic, průměrná výška 1.86), případně Big Four, když počítáme Murrayho (1.9 m), a pak nástupem vysoké "Next Gen", mezi které patří Medvedev (1.98 m), Tsitsipas (1.93 m), Zverev (1.98 m) nebo Berrettini (1.96 m). Jistý výkyv také jistě způsobili "Serveboti" Isner (2.08 m) a Raonic (1.96 m).


![linear](https://user-images.githubusercontent.com/83585883/175540702-739ee5fd-ded9-477d-b895-34a1544e9fd4.png)  

Proložení přímkou nereflektuje propad v devadesátých letech (kdy na špičce byla spousta nižších hráči, např. Agassi, Chang, Hewitt, Muster).  
Proto je R^2, coefficient of determination, cca 0,53, tedy nepříliš uspokojivé číslo.  
Stále však můžeme konstatovat, že tenisoví nestoři měli svým způsobem pravdu, od 70. let se průměrná výška top 10 hráčů zvedla o zhruba 10 cm a rostoucí trend je zřetelný i v posledních několika letech.

#### Na závěr: Overfitting example

Kauzální vztah mezi plynoucím časem a rostoucí výškou tenistů nejspíše nebude odpovídat polynomu třetího stupně (přestože právě graf kubické funkce lze v datech vidět), abych ale ilustroval problém overfittingu, kdy model ušijeme přesně na míru naměřeným datům, získáme dobré výsledky, ale zhoršíme tak jeho obecnou výpovědní hodnotu a schopnost přesně předpovídat další výsledky, zkusím data napasovat na kubickou polynomiální regresi.
Tímto způsobem dostaneme hodnotu R^2 0.7.

![polynomial](https://user-images.githubusercontent.com/83585883/175540752-35060b0c-a2c3-4fdf-b02a-154d5b7c9543.png)

