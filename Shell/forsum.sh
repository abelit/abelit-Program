#!/bin/sh

i=0
sum=0
plussign='+ '
endnum=20
while [ $i -lt $endnum ]
	do
		i=$[$i+1]
		sum=$[$sum + $i]
		if [ $i = $endnum ];then
			plussign='= '
		fi
		echo -n "$i" "$plussign"
		sleep 0.5
	done
echo $sum
