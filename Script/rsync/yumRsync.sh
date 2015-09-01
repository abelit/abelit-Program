#!/bin/bash
#Script name:yumRsync.sh

RsyncBin="rsync"
RsyncPerm="-avrt --delete --no-iconv --bwlimit=1000"

#directories for storing softpackage
centos_7='/var/www/html/yum_repo/centos/7.1.1503/'
epel='/var/www/html/yum_repo/epel/7/'
epel_testing='/var/www/html/yum_repo/epel/testing/7/'
openstack_juno='/var/www/html/yum_repo/repos/openstack/openstack-juno/el7/'
openstack_kilo='/var/www/html/yum_repo/repos/openstack/openstack-kilo/el7/'

#source 
scentos_7='rsync://mirrors.yun-idc.com/centos/7.1.1503/'
sepel='rsync://mirrors.yun-idc.com/epel/7/'
sepel_testing='rsync://mirrors.yun-idc.com/epel/testing/7/'

#rsync logfile
LogFile='/var/www/html/yum_repo/yumRsyncLog'
Date=`date +%Y-%m-%d`

dirList="$centos_7 $epel $epel_testing $LogFile"
sourceList="centos_7 epel epel_testing openstack_juno openstack_kilo"

#check the result of rsync
function check() {
	if [ $? -eq 0 ];then
		echo -e "\033[1;32mRsync is success!\033[0m" >>$LogFile/$Date.log
		echo -e "\033[1;32mRsync is success!\033[0m"
	else
		echo -e "\033[1;31mRsync is fail!\033[0m" >>$LogFile/$Date.log
		echo -e "\033[1;31mRsync is fail!\033[0m"
	fi
}

#configure the directories that store softpackage
function dirConfig() {
	for list in $dirList
		do
			if [ ! -d "$list" ];then
				mkdir -p $list
			fi
		done
}

#define default rsyncStart
function rsyncStart() {
	dirConfig

	for slist in $sourceList
		do
			if [ $slist = "centos_7" ];then
				echo "Now start to rsync $slist" >>$LogFile/$Date.log
				$RsyncBin $RsyncPerm  --exclude isos $scentos_7 $centos_7 >>$LogFile/$Date.log
				centoscheck="`check`"
			elif [ $slist = "epel" ];then
				echo "Now start to rsync $slist" >>$LogFile/$Date.log
				$RsyncBin $RsyncPerm --exclude ppc64  $sepel $epel >>$LogFile/$Date.log
				epelcheck="`check`"
			elif [ $slist = "epel_testing" ];then
				echo "Now start to rsync $slist" >>$LogFile/$Date.log
				$RsyncBin $RsyncPerm  --exclude ppc64 $sepel_testing $epel_testing >>$LogFile/$Date.log
				epel_testingcheck="`check`"
			fi
		done
	echo ""
	echo "----------------------------------------------------------------------------------------"
	echo "yum-packages rsync hava been finished!" &&  echo "yum-packages rsync hava been finished!" >>$LogFile/$Date.log
	echo "The detail of all yum-packages:" &&   echo "The detail of all yum-packages:" >>$LogFile/$Date.log
	echo "The centos rsync status:$centoscheck" && echo "The centos rsync status:$centoscheck" >>$LogFile/$Date.log
	echo "The epel rsync status:$epelcheck" && echo "The epel rsync status:$epelcheck" >>$LogFile/$Date.log
	echo "The epel_testing rsync status:$epel_testingcheck" &&  echo "The epel_testing rsync status:$epel_testingcheck" >>$LogFile/$Date.log
	echo "----------------------------------------------------------------------------------------"
	
}

#call rsyncStart
rsyncStart
