<h2>OADOI Python3 script</h2>
Følgende script udtrækker x antal poster fra unpaywall API indeholdende OA metadata.
Læs information i scriptet for mere information. Scriptet afvikles ved at placere dette script oadoi.py og datasæt.csv i samme folder og kalde kommandoen python oadoi.py fra terminal (Linux eller Mac) eller commandline (Windows).
Output til skærm og til filen datasæt.json. Parametre kan ændres i scriptet.

Download koden her: https://github.com/enemydown-dk/BF_API/blob/master/filer/oadoi.py

**Kode:**
```python
#!/usr/bin/env python3

"""Doi lookup i unpaywall API via doi fra csv-fil"""

import urllib.request
import urllib.error
import json
import csv

"""
Funktionalitet og begrænsning:
Dette script udtrækker Open Access informationer fra unpaywall.org baseret på en
doi-liste bestående af en eller flere doi'er. Det genererede datasæt
(datasæt.json vil bestå af x antal enkeltstående json responses, da unpaywall
ikke tillader multiple query parameters :-(

Script er skrevet med det formål, at give nybegyndere en simpel tilgang til at
programmere i Python3. Funktionalitet er derfor lavet så simpel som muligt, så
flow i programmet er let at følge.
"""

URL = 'https://api.unpaywall.org/v2/' #URL til API'et
MAIL = 'asger.hansen@gmail.com' #angiv din e-mail her, påkrævet for at undgå blacklist.
FILE_NAME = 'datasæt.csv' #angiv filnavn på den fil der indeholder din DOI-liste.
JSON_NAME = 'datasæt.json' #angiv et filnavn på den fil, hvor du ønsker output.

def pull_data(url):
    """Udfører forespørgslen i API og returnerer evt. fejlkoder til terminal"""
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        write_csv(JSON_NAME, data)
        print(data)

    except urllib.error.HTTPError as _:
        print(_.reason)

def write_csv(json_name, data):
    """Open filen i variablen JSON_NAME i append format, og skriver herefter data"""
    with open(json_name, mode="a") as file:
        file.write(json.dumps(data))

def main():
    """Åbner filen i variablen FILE_NAME og læser DOI en efter en + kalder pull_data"""
    with open(FILE_NAME, newline='') as _:
        reader = csv.reader(_)
        for row in reader:
            pull_data(URL + row[0] + '?email=' + MAIL)

if __name__ == '__main__':
    main()

```
<h2>OADOI BASH script</h2>
Bash er en kommandofortolker, som indgår i GNU-projektet. Den er almindeligt forekommende i Unix-lignende operativsystemer, desuden er den forudinstalleret som kommandofortolker i Mac OS X. Scriptet foretager det samme som ovenstående Python script, men er dog langt kortere. Scriptet afvikles ved at downloade scriptet oadoi.sh og køre kommandoen 'chmod u+x oadoi.sh' hvilket giver dig (user) kørsels (execution) rettigheder på filen. Gør du ikke dette vil du få 'adgang nægtet/permission denied'.
Script kan nu afvikles med kommandoen ./oadoi.sh

Download koden her: https://github.com/enemydown-dk/BF_API/blob/master/filer/oadoi.sh

**Kode:**

```bash

#!/bin/bash

filename=./datasæt.csv
while read line || [[ -n "$line" ]]; do
    echo $line
    curl -o datasæt.json https://api.unpaywall.org/v2/$line?email=asger.hansen@gmail.com
done < "$filename"
```

Eksperimenter eventuelt med at videreudbygge scriptet. Du kan finde mere information om curl ved at skrive 'man curl' i terminal.

<h2>SCIDOI Python3 script</h2>
Følgende script udtrækker x antal poster fra Science Direct API indeholdende OA metadata.
Scriptet afvikles ved at placere dette script scidoi.py og datasæt.csv i samme folder og kalde kommandoen python scidoi.py fra terminal (Linux eller Mac) eller commandline (Windows). Output til skærm og til filen datasæt.json. Parametre kan ændres i scriptet. BEMÆRK: Du kan ikke anvende scriptet uden at have en API nøgle fra udbyderen (Elsevier). Den kan umiddelbart skaffes ved henvendelse. Scriptet er inkluderet som et eksempel på variation ift. at benytte samme fremgangsmåde til et andet API.


```python
#!/usr/bin/env python3

"""
Script til at udtrække OA metadata from Science Direct API.
Brugen forudsætter at man er i besidelse af en API-nøgle.
"""

import urllib.request
import urllib.error
import json
import csv

APIKEY = 'indsæt_nøgle_her' #indtast din APIkey fra Science Direct her.
FILE_NAME = 'datasæt.csv' #navn på inputfil her.
JSON_NAME = 'datasæt.json' #navn på output fil her.

def pull_data(url):
    """Opslag i Science Direct API"""
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        write_csv(JSON_NAME, data)
        print(data)

    except urllib.error.HTTPError as _:
        print(_.reason)

def write_csv(json_name, data):
    """Skriver datastrøm (json) til outputfilen i variablen JSON_NAME"""
    with open(json_name, mode="a") as file:
        file.write(json.dumps(data))

def main():
    """Læser inputfilen i variablen FILE_NAME"""
    with open(FILE_NAME, newline='') as _:
        reader = csv.reader(_, delimiter=';')
        for row in reader:
            wos_url = "https://api.elsevier.com/content/article/doi/" \
            + row[0] + "?apiKey=" + APIKEY + "&httpAccept=application%2Fjson"
            pull_data(wos_url)

if __name__ == '__main__':
    main()
```
