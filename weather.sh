URL='https://aviationweather.gov/metar/data?ids=LFMP&format=raw&date=&hours=0'

[ -f metar.html ] || wget -q -O metar.html "$URL"
[ $? -ne 0 ] && exit 2

DATA=$(sed -n -e '/^<!-- Data starts here -->$/,/^<!-- Data ends here -->$/'{'/^<!-- Data starts here -->$/d;/^<!-- Data ends here -->$/d;p'} metar.html | tr -d '\n' | sed -n -e 's/^<code>LFMP \(.*\)<\/code>.*$/\1/p')

#echo $DATA

if [ -z "$DATA" ]
then
    [ -d erreurs ] || mkdir erreurs
    mv metar.html erreurs/
    exit 1
else
    rm metar.html
fi

AN=$(date +%Y)
MOIS=$(date +%m)

RAWTIME=$(echo $DATA | sed -e 's/^\([0-9]\{6\}\)Z.*$/\1/')
RAWTEMP=$(echo $DATA | cut -d' ' -f 6 | tr 'M' '-')
PRESSION=$(echo $DATA | cut -d' ' -f 7 | tr -d 'Q')
JOUR=${RAWTIME:0:2}
HEURE=${RAWTIME:2:2}
MIN=${RAWTIME:4:2}
TEMP=$(echo $RAWTEMP | cut -d'/' -f 1)
ROSEE=$(echo $RAWTEMP | cut -d'/' -f 2)

[ -f metar.dat ] || echo '       DATE         |T°|TR| P' > metar.dat

DERNIERE_MESURE=$(tail -1 metar.dat | cut -d '|' -f1)
if [ "$DERNIERE_MESURE" != "$AN-$MOIS- $JOUR $HEURE:$MIN:00" ]
then
    echo "$AN-$MOIS- $JOUR $HEURE:$MIN:00|$TEMP|$ROSEE|$PRESSION" >> metar.dat
    #echo "INSERT INTO metar VALUES ('$AN-$MOIS- $JOUR $HEURE:$MIN:00',$TEMP, $ROSEE, $PRESSION);" | sqlite3 metar.db
