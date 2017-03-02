
USAGE :
ajouter la ligne ci-dessous, commentaire retiré, au .profile ::

    . $HOME/ehtools/ehtools-init

Des variables doivent recevoir des valeurs...
par ex. dans .profile appelant

ECDOC : nom du host qui héberge ``teb`` et ``tebl``

DEV : chemin absolu du répertoire qui contient les répertoires de dev::

      export DEV="$HOME/dev"

DEVREPFILE : chemin absolu du fichier qui contient la liste des répertoires
de dev. Spécifique à chaque personne/environnement
un nom de répertoire par ligne
Ce doit être une variable d'environnement::

             export DEVREPFILE="$HOME/ehtools/etc/myreps.txt"



