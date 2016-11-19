#!/bin/bash
#Script name:centos_yum_rsync.sh

RsyncBin="rsync"
RsyncPerm="-avrt --delete --no-iconv --bwlimit=1000"
centos_7='/var/www/html/yum_repo/centos/7.1.1503/'
LogFile='/var/www/html/yum_repo/centos/centos_rsync_yum_log'
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
if [ ! -d "$centos_7" ];then
		mkdir -p $centos_7
fi

if [ ! -d "$LogFile" ];then
    mkdir -p $LogFile
fi
}

#define rsyncStart
function rsyncStart {
dirConfig
echo 'Now start to rsync centos 7!' >>$LogFile/$Date.log
$RsyncBin $RsyncPerm  --exclude isos rsync://mirrors.yun-idc.com/centos/7.1.1503/ $centos_7 >>$LogFile/$Date.log
check
}

#call rsyncStart
rsyncStart