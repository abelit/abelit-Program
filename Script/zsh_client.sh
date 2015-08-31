#!/bin/zsh
#zsh TCP client program
zmodload zsh/net/tcp

ztcp localhost 5150
hostfd=$REPLY

read line <& $hostfd
echo $line

while [ 1 ]
	do
		echo -n "Enter text:"
		read phrase
		echo Sending $phrase to remote host ...
		echo $phrase >& $hostfd
		if [[ $phrase = "exit" ]]
		then
			break
		fi
		read line <& $hostfd
		echo "	Received:$line"
	done
ztcp -c $hostfd
%
