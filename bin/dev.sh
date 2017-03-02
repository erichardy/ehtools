#!/bin/sh

touch /tmp/dialogtmp && FICHTMP=/tmp/dialogtmp
trap "rm -f $FICHTMP" 0 1 2 3 5 15
CHOICES="$HOME/ehtools/etc/choices.txt"
DEV="$HOME/Dev"

IFS="
"
DIALOG=${DIALOG=dialog}

L=`grep -v '#' $CHOICES`
nb=1
for R in $L
do
  if [ $nb = 1 ]
  then
    LL="$nb $R"
  else
    LL="$LL $nb $R"
  fi
  nb=`expr $nb + 1`
done
IFS=" "
$DIALOG --clear --title "Choisir..." --menu "Choisir : " 30 40 14 $LL 2> $FICHTMP

NBREP=`cat $FICHTMP`
REP=`head -$NBREP $CHOICES | tail -1`

case $? in
    0)  echo $DEV/$REP > $HOME/ehtools/tmp/devREP;;
    1)  echo "Annulé";;
    255)    echo "Appuyé sur Echap. ";;
esac


