bak_exist() { 
    echo $fic  | grep -E '^.*\.bak' > /dev/null 2>&1 #le fichier ccommence par n'importe quoi et ce termine en .bak
    return $?

}

n=0

for fic in *
do
    if [ -f $fic ]
    then
        bak_exist $fic
        [ $? -eq 0 ] && continue
        echo $fic
        if [ ! -f "$fic.bak" ] 
        then
            cp "$fic" "$fic.bak"
            n=$(( $n + 1 ))
        fi
    fi
done

echo "$n fichier(s) sauvegardé(s)"