#backup and save BDD

PGHOST='127.0.0.1' #Adress Hosting
PGPORT='5432'      #Adress PORT
PGUSER='postgres'  #USER access
DUMP=/usr/bin/pg_dump
SQL=/usr/bin/psql

REP=/var/backups/postgres

JOUR=$(date +%d)

[ -d $REP/$JOUR ] || mkdir -p $REP/$JOUR


echo '\l' | $SQL -h $PGHOST -p $PGPORT -U $PGUSER | cut -d'|' -f1 | sed -n -e '4,$p'

#grep -v [n'affiche pas les motif en corespondance]
# grep -v -E '^[ ]*$' [supprime les tab ou encore les espace]
grep -v  template | grep -v rows\) | grep -v -E '^[ ]*$'

for base in "$BASE"
do
# $? dernière variable utilisé
# -n pas de saut de ligne
# -Fc format Custom de sauvegarde
    echo -n "Sauvegarde de la BDD $base..."
    $DUMP -h $PGHOST -p $PGPORT -U $PGUSER -Fc -f "$REP/$JOUR/$base.backup" $base
    if [ $? -eq 0 ]
    then
        echo OK
        gzip "$REP/$JOUR/$base.sql"
    else
        echo ERROR
    fi
done

# Utilisation possible sur crontab pour backup save  auto
