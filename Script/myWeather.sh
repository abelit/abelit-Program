#!/bin/bash
# extract the current weather for Chicago. IL

URL="http://weather.yahoo.com/united-states/illinois/chicago-2379574/"
LYNX=`which lynx`
TMPFILE=`mktemp tmpXXXXXX`
$LYNX -dump $URL > $TMPFILE
conditions=`cat $TMPFILE | sed -n -f sedcond`
temp=`cat $TMPFILE | sed -n -f sedtemp`
rm -f $TMPFILE
echo " Curren conditions: $conditions"
echo The current temp outside is: $temp

