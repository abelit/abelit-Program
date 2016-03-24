#!/bin/sh

if [ -f ~/.profile ]; then
        . ~/.profile
fi

ORACLE_SID=$1;
export  ORACLE_SID=$ORACLE_SID

echo "Archivelog of $ORACLE_SID Clean Start Time: `date`">>/home/oracle/archivelog_clean/clean.log

$ORACLE_HOME/bin/rman log=/home/oracle/archivelog_clean/rman.log <<EOF
connect target /
run{
crosscheck archivelog all;
delete noprompt expired archivelog all;
delete noprompt archivelog all completed before 'sysdate - 3';
}
exit;
EOF
echo "Archivelog Of $ORACLE_SID  Clean End Time: `date`">>/home/oracle/archivelog_clean/clean.log
~

