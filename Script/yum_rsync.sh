#!/bin/bash
#Script name:yum_rsync.sh
RsyncBin="rsync"
RsyncPerm="-avrt --delete --no-iconv --bwlimit=1000 --exclude isos"
centos_7='/home/chenying/Documents/yum_repo/centos/7.1.1503/'
LogFile='/home/chenying/Documents/yum_repo/rsync_yum_log'
Date=`date +%Y-%m-%d`
#check
function check {
if [ $? -eq 0 ];then
    echo -e "\033[1;32mRsync is success!\033[0m" >>$LogFile/$Date.log
else
    echo -e "\033[1;31mRsync is fail!\033[0m" >>$LogFile/$Date.log
fi
}
if [ ! -d "$LogFile" ];then
    mkdir $LogFile
fi
#rsync centos 7
echo 'Now start to rsync centos 7!' >>$LogFile/$Date.log
$RsyncBin $RsyncPerm rsync://mirrors.yun-idc.com/centos/7.1.1503/ $centos_7 >>$LogFile/$Date.log
check
