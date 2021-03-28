#!/bin/bash




#
# On vide successivement les chaines par défaut
#

iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD


#
#On vide d’autres chaines, dans d’autres contextes. On verra plus tard l’intérêt.
#

iptables -t nat -F POSTROUTING
iptables -t nat -F PREROUTING
iptables -t raw -F PREROUTING
iptables -t raw -F OUTPUT

# On vide et on détruit une chaine "utilisateur" LOGDROP
# qui n’existe pas forcément, mais on ne s’en inquiète pas trop

iptables -F LOGDROP
iptables -X LOGDROP


#On créé la chaine utilisateur LOGDROP qui va successivement
#journaliser les paquets avec un FW_DENIED devant (notez l’espace après)
#puis jeter les paquets
#

iptables -N LOGDROP
iptables -A LOGDROP -j LOG --log-prefix "FW_DENIED "
iptables -A LOGDROP -j DROP

