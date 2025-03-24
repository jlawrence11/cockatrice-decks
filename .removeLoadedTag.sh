#!/bin/bash

for f in */*.cod; do
    # do some stuff here with "$f"
    # remember to quote it or spaces may misbehave
    xmlstarlet ed -d "//lastLoadedTimestamp" "./$f" > "tmp.tmp"
    mv tmp.tmp "./$f"
done
