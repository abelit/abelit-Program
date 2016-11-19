#!/bin/bash
#Script name:yum_rsync.sh
RsyncBin="rsync"
RsyncPerm="-avrt --delete --no-iconv --bwlimit=1000 --exclude isos"
openstack='/home/chenying/Documents/yum_openstack/repos/openstack/openstack-juno/'
LogFile='/home/chenying/Documents/yum_openstack/rsync_yum_log'
Date=`date +%Y-%m-%d`
mkdir -p $openstack
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
echo 'Now start to rsync openstack' >>$LogFile/$Date.log
$RsyncBin $RsyncPerm https://repos.fedorapeople.org/repos/openstack/openstack-juno/epel-7 $openstack >>$LogFile/$Date.log
check
