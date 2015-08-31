#!/bin/bash
#Script name:epel_testing_yum_rsync.sh

RsyncBin="rsync"
RsyncPerm="-avrt --delete --no-iconv --bwlimit=1000"
epel_testing='/var/www/html/yum_repo/epel/testing/7/'
LogFile='/var/www/html/yum_repo/epel/epel_testing_rsync_yum_log'
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
    mkdir -p $epel_testing
fi

if [ ! -d "$LogFile" ];then
    mkdir -p $LogFile
fi
}

#define rsyncStart
function rsyncStart {
dirConfig
echo 'Now start to rsync epel-testing 7!' >>$LogFile/$Date.log
$RsyncBin $RsyncPerm --exclude ppc64 rsync://mirrors.yun-idc.com/epel/testing/7/ $epel_testing >>$LogFile/$Date.log
check
}

#call rsyncStart
rsyncStart