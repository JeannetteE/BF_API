#!/bin/bash
filename=./datasæt.csv
while read line || [[ -n "$line" ]]; do
    echo $line
    curl -o datasæt.json https://api.unpaywall.org/v2/$line?email=asger.hansen@gmail.com
done < "$filename"
