#!/bin/bash
#Script name:epel_yum_rsync.sh

RsyncBin="rsync"
RsyncPerm="-avrt --delete --no-iconv --bwlimit=1000"
epel='/var/www/html/yum_repo/epel/7/'
LogFile='/var/www/html/yum_repo/epel/epel_rsync_yum_log'
Date=`date +%Y-%m-%d`

#check the result of rsync
function check {
if [ $? -eq 0 ];then
    echo -e "\033[1;32mRsync is success!\033[0m" >>$LogFile/$Date.log
else
    echo -e "\033[1;31mRsync is fail!\033[0m" >>$LogFile/$Date.log
fi
}

#configure the directories that store softpackage
function dirConfig {
if [ ! -d "$epel" ];then
    mkdir -p $epel
fi

if [ ! -d "$LogFile" ];then
    mkdir -p $LogFile
fi
}

#define rsyncStart
function rsyncStart {
dirConfig
echo 'Now start to rsync epel 7!' >>$LogFile/$Date.log
$RsyncBin $RsyncPerm --exclude ppc64 rsync://mirrors.yun-idc.com/epel/7/ $epel >>$LogFile/$Date.log
check
}

#call rsyncStart
rsyncStart