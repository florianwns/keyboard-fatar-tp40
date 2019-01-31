# DIY - CUSTOM KEYBOARD - FATAR TP/40L

Voici quelques notes de travail sur la construction d'un contrôleur MIDI en me servant de la base d'un FATAR TP/40L récupéré sur un Kurzweil PC3X.

J'ai grâce au projet Open-Source MIDIBOX NG, réussi à créer mon propre clavier maître.
Le tout fonctionne à la perfection, mais demande d'y consacrer pas mal de temps.



## MIDIBOX NG 

Il existe plusieurs projet MIDIBOX mais j'ai choisi MIDIBOX NG car j'avais besoin de modifier la courbe de vélocité du clavier, ce qui n'était pas possible avec le projet MIDIBOX KB.

Vous trouverez toute les infos nécessaire sur la page du projet : http://www.ucapps.de/midibox_ng.html


## FATAR TP/40L

J'ai eu besoin de 3 cartes électronique pour réaliser ce projet : 

- "MIDIbox Core STM32F4 PCB" qui accueille le STM32F4 (https://modularaddict.com/manufacturer/midibox/midibox-core-stm32-pcb)
- "MIDIbox DIO Matrix PCB" qui permet de relier les matrices de leds (https://modularaddict.com/manufacturer/midibox/midibox-diomatrix-pcb)
- une qui rend compatible le "MIDIbox DIO Matrix PCB" avec le clavier Fatar, vous devez la faire imrpimer, mais le PCB est dispo ici. Elle a été créée par un membre de la communauté MIDIBOX, FantomXR que je remercie grandement (http://www.midibox.org/dokuwiki/doku.php?id=fantomxr).


Dans mon cas, j'ai découpé le clavier FATAR pour qu'il ne fasse plus que 72 touches, cela ne pose pas de soucis majeurs, mais faites attentions à ne pas découpé les matrices de leds, sinon faudra resouder tout ça ;) 

Pour info, un thread assez intéressant où l'on trouve la liste des touchers piano par modèle de clavier : https://www.gearslutz.com/board/electronic-music-instruments-and-electronic-music-production/1149168-ultimate-keybed-thread-models-manufacturers-listed.html



## CONNECTIQUES

Le clavier maître est relativement simple puisqu'on peut y brancher une pédale de sustain et une pédale d'expresion. Le système MIDIBOX étant modulaire, on peut très bien imaginer rajouter par la suite des potards, une modulation, des LCDs, etc...

Il suffira soit de connecter un Module AINSER64 (http://www.ucapps.de/mbhp_ainser64.html), ou de d'utiliser le connectiques J5A et J5B.

Petite Astuce : Si vous alimenter votre carte en USB comme moi, la tension n'est pas forcément très stable et du coup le contrôleur envoie masse de messages MIDI car les valeurs varient avec la tension. Du coup il existe une petite technique pour lisser les valeurs et éviter les variations, c'est de mettre un condensateur de 100nf entre la masse et l'entrée analogique au plus proche du contrôleur.

Aussi il faut le savoir les pédales d'expression sont alimentés en 3.3 volt ;) 



## COURBE DE VÉLOCITÉ

Mon plus gros soucis, lors de la création du contrôleur a été la vélocité du clavier. Elle ne me correspondait pas vraiment, du coup j'ai mis au point une petite technique.

Par défaut j'ai mis une courbe de vélocité linéaire dans mon fichier de config .NGC, puis j'ai installé la démo gratuite de Pianoteq, et j'ai testé plusieurs courbes correctrice de vélocité dispo sur leur site (https://www.pianoteq.com/velocity_curves). Une fois ma courbe de vélocité trouvé dans Pianoteq, j'ai codé un petit programme en python pour convertir les courbes de vélocité Pianoteq au format MIDIBOX NG et je l'ai rentrée dans mon fichier de configuration.

Je me suis aussi servi de MIDI MONITOR (https://www.snoize.com/MIDIMonitor/) pour vérifier que j'arrivait bien à obtenir une vélocité bien équilibré sur l'ensemble des 128 niveaux.



## INSTALLATION SUR MAC OS

Avant d'installer MIOS STUDIO (http://www.ucapps.de/mios_studio.html) qui permet de configurer la carte électronique et charger le firmware, vous devez sous MAC démarrer avec CMD+R et dans le terminal faire un 'csrutil disable', sinon la carte ne sera pas reconnu par MAC OS.

Après il vous suffit d'installer le firmware, et de charger votre fichier de configuration qui sera stocké sur la carte SD. 










