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
