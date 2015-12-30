#! /bin/bash

#===============================================================================================
#   System Required:  CentOS7.x (64bit)
#   Version:3.141
#   Description: Build Hadoop and Spark Cluster Based on CentOS
#   Author: ChenYing <ychenid@live.com>
#   Intro:  http://www.dockertime.com 
#===============================================================================================

# Include shell environment
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
clear

# Show author's info.
echo "########################################################################"
echo "# Build Hadoop Cluster and Spark Based on CentOS 7.x (64bit)           #"
echo "# Version:3.141                                                                     #"
echo "#       Author: ChenYing <ychenid@live.com>                            #"
echo "#       Intro: http://www.dockertime.com                               #"
echo "#                                                                      #"
echo "########################################################################"
echo ""

# Make sure only root can run this script
function rootness(){
	if [[ $EUID -ne 0 ]]; then
		echo "Error:This script must be run as root!" 1>&2
		exit 1
	fi
}

# Check whether docker has been installed or not
function isDocker(){
	dk=`rpm -qa | grep docker`	
	if [[ "$dk" = "" ]];then
		echo "Warnning: !! No docker service installed on your system."	
		echo "Now docker service will be installed on your system,please wait ..."
		yum install -y docker
	fi	
}

# Start docker service
function startDocker(){
	systemctl restart docker.service
}

# Define variable --------------Begin

# Define hadoop and spark's path
export current_path=`pwd`
package_path="$current_path/cluster_package"
if [[ ! -d "$package_path" ]];then
	echo "Please input the path of 'cluster_package'!"
	read package_path
 	package_path="$package_path/cluster_package"
fi

# Define file known_hosts and its path
dockerconf_path=$package_path/dockerconf
known_hosts_path=$dockerconf_path/known_hosts

# Define hadoop and its conf's path
hadoop_path=$package_path/hadoop-2.7.0
hadoopconf_path=$hadoop_path/etc/hadoop
hadoop_slaves_path=$hadoopconf_path/slaves

# Define spark and its conf's path
spark_path=$package_path/spark-1.3.1-bin-hadoop2.6
sparkconf_path=$spark_path/conf
spark_env_path=$sparkconf_path/spark-env.sh
spark_slaves_path=$sparkconf_path/slaves

# Define dnsconf path
dnsconf_path=$package_path/dnsconf

# Define docker image name or tag
docker_image="centos:hadoop"

# Define variable --------------End

# Configure soft path environment
function pathEnvironment(){
		# Check dockerconf's path
		if [ -d "$dockerconf_path" ]
		then
			# Check the path of known_hosts
			if [ -e "$known_hosts_path" ];then
				touch $known_hosts_path
			fi
		else
			mkdir  -p $dockerconf_path
			# Check the path of known_hosts
			if [ -e "$known_hosts_path" ];then
				touch $known_hosts_path
			fi
		fi
			
		# Check hadoop path
		if [ -d "$hadoop_path" ]
		then
			# Check the path of hadoop's slaves conf
			if [ ! -e "$hadoop_slaves_path" ];then
				touch $hadoop_slaves_path
			fi
		else
			mkdir -p $hadoop_path
			# Check the path of hadoop's slaves conf
			if [ ! -e "$hadoop_slaves_path" ];then
				touch $hadoop_slaves_path
			fi
		fi
		
		# Check spark path
		if [ -d "$spark_path" ]
		then
			# Check the pathe of spark's slaves conf
			if [ ! -e "$spark_slaves_path" ];then
				touch $spark_slaves_path
			fi
			# Check the path of spark-en.sh  conf
			if [ ! -e "$spark_env_path" ];then
				touch $spark_env_path
			fi
		else
			mkdir -p $spark_path
			# Check the pathe of spark's slaves conf
			if [ ! -e "$spark_slaves_path" ];then
				touch $spark_slaves_path
			fi
			# Check the path of spark-en.sh  conf
			if [ ! -e "$spark_env_path" ];then
				touch $spark_env_path
			fi
		fi
		
}

#Run docker container
function startContainer(){
	function startdnsContainer(){
		#Start a dns (which is based dnsmasq server) container
		docker run -t -d --name dns -h dns -v $known_hosts_path:/root/.ssh/known_hosts -v $dnsconf_path:/etc/dnsmasq.d/ $docker_image 

		#Get ip address of the running container
		dns_container='dns'
		dns_ip=$(docker inspect $dns_container | grep IPAddress | cut -f4 -d '"')
		echo "host-record=$dns_container,$dns_ip" > /etc/dnsmasq.d/host_$dns_container

		echo ""
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo "The dns container has been started."
		echo "The name of container:${dns_container}."
		echo "The IPAddress: ${dns_ip}"
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo ""
	}

	function startHadoopContainer(){
		#Get ip address of the running container
		dns_container='dns'
		dns_ip=$(docker inspect $dns_container | grep IPAddress | cut -f4 -d '"')
		
		
		#Start a master hadoop container (Namenode/Master)
		docker run -t -d --dns=$dns_ip --name master -h master -v $known_hosts_path:/root/.ssh/known_hosts -v $package_path:/usr/local $docker_image
		master_container='master'
		master_ip=$(docker inspect $master_container | grep IPAddress | cut -f4 -d '"')
		echo "host-record=$master_container,$master_ip" > $dnsconf_path/host_$master_container	
		echo "export JAVA_HOME=/usr/java/jdk1.8.0_25"  >> $spark_env_path
		echo "export SCALA_HOME=/usr/local/scala-2.10.5" >> $spark_env_path
		echo "export SPARK_WORKER_MEMORY=1g" >> $spark_env_path
		echo "export SPARK_MASTER_IP=$master_ip" >> $spark_env_path
		echo "export MASTER=spark://$master_ip:7077" >> $spark_env_path
		echo "export HADOOP_CONF_DIR=/usr/local/hadoop-2.7.0/etc/hadoop" >> $spark_env_path

		echo ""
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo "The namenode(master) has been started."
		echo "The name of container:${master_container}."
		echo "The IPAddress: ${master_ip}"
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo ""

		#Start a master hadoop container (SecondaryNamenode/Master)
		docker run -t -d --dns=$dns_ip --name secondarynamenode -h secondarynamenode -v $known_hosts_path:/root/.ssh/known_hosts -v $package_path:/usr/local $docker_image
		master_container='secondarynamenode'
		master_ip=$(docker inspect $master_container | grep IPAddress | cut -f4 -d '"')
		echo "host-record=$master_container,$master_ip" > $dnsconf_path/host_$master_container	
		echo "export JAVA_HOME=/usr/java/jdk1.8.0_25"  >> $spark_env_path
		echo "export SCALA_HOME=/usr/local/scala-2.10.5" >> $spark_env_path
		echo "export SPARK_WORKER_MEMORY=1g" >> $spark_env_path
		echo "export SPARK_MASTER_IP=$master_ip" >> $spark_env_path
		echo "export MASTER=spark://$master_ip:7077" >> $spark_env_path
		echo "export HADOOP_CONF_DIR=/usr/local/hadoop-2.7.0/etc/hadoop" >> $spark_env_path

		echo ""
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo "The secondarynamenode(master) has been started."
		echo "The name of container:${master_container}."
		echo "The IPAddress: ${master_ip}"
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo ""

		#Start some slave hadoop container (Datanode/Slaves)
		echo "Please the number of Datanode that you want to build: "
		read -p "(Default will create 5 datanodes):" number
		if [ "$number" = "" ];then
			number=5
		fi
		while [ $number -gt 0 ]
		do
			docker run -t -d --dns=$dns_ip --name slave${number} -h slave${number} -v $known_hosts_path:/root/.ssh/known_hosts -v $package_path:/usr/local $docker_image
			slave_container="slave${number}"
			slave_ip=$(docker inspect $slave_container | grep IPAddress | cut -f4 -d '"')
			echo "host-record=$slave_container,$slave_ip" > $dnsconf_path/host_$slave_container

			echo "export JAVA_HOME=/usr/java/jdk1.8.0_25"  >> $spark_env_path
			echo "export SCALA_HOME=/usr/local/scala-2.10.5" >> $spark_env_path
			echo "export SPARK_WORKER_MEMORY=1g" >> $spark_env_path
			echo "export SPARK_MASTER_IP=$master_ip" >> $spark_env_path
			echo "export MASTER=spark://$master_ip:7077" >> $spark_env_path
			echo "export HADOOP_CONF_DIR=/usr/local/hadoop-2.7.0/etc/hadoop" >> $spark_env_path

			echo ""
			echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
			echo "The datanode slave${number} has been started."
			echo "The name of container:${slave_container}."
			echo "The IPAddress: ${slave_ip}"
			echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
			echo ""
			number=$[ $number-1 ]
		done

	}
	startdnsContainer
	startHadoopContainer
}

#Use Hadoop
function enterHadoop(){
	echo "Now you can go to the node of hadoop. Default you will go to the master node."
	echo "If you don't know which node you have started and you can input 'node' to show."
	echo "Please input the name of node you will go to:"
	read -p "(Default is master node.):" node
	if [ "$node" = "" ];then
		node='master'	
	else
		if [ "$node" = "node" ];then
			list="`docker ps | grep -E "slave|master|secondarynamenode|dns" | awk '{print $NF}'`"
			echo $list
			enterHadoop
		fi
		node=$node
	fi
	docker-enter $node
}


#Restart dnsmasq service in the dns server
function restartdns(){
	docker-enter dns /usr/sbin/dnsmasq
}

#Reset Docker
function resetDocker(){
	rm -f $dnsconf_path/*
	cat /dev/null > $known_hosts_path #Clear known_hosts contents OR you can use command "echo "" > /usr/local/dockerconf/known_hosts" 
	#delete the lines include "export" as the first word
	sed -i '/^export/d' $spark_env_path
	#list1="`docker ps | grep -E "slave|master|secondarynamenode|dns" | awk '{print $NF}'`" #Get the name of hadoop container
	list="`docker ps -a | grep -E "slave|master|secondarynamenode|dns" | awk '{print $NF}'`" #Get the name of hadoop container
	#Stop Container
	function stopContainer(){
		for container_name in $list
		do
			echo "The Hadoop Node `docker stop $container_name` has been stoped! "
		done
	}
	
	#Romove Container
	function rmContainer(){
		for container_name in $list
		do
			echo "The Hadoop Node `docker rm $container_name` has been removed! "
		done
	}
	
	if [ "$list" != "" ];then
		echo "This will clear and remove all hadoop container! "
		echo "Now the docker is stopping container ... "
		stopContainer
		echo "Now the docker is removing container ... "
		rmContainer
	
		
	else
		echo "The hadoop container maybe have been cleared and removed. No created or running hadoop container exits."
		
	fi

	#Call makesymble function
	makeSymble
	#Call headinfo function
	headInfo
}

#Look up whether there have some created or running hadoop container
function checkContainer(){
	list1="`docker ps | grep -E "slave|master|secondarynamenode|dns"`"
	list2="`docker ps -a | grep -E "slave|master|secondarynamenode|dns"`"
	if [ "$list1" != "" ];then
		#Running
		echo "There have some running hadoop container."
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		docker ps | grep -E "slave|master|secondarynamenode|dns"
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo ""
	else
		echo "No hadoop container is running."
	fi
	

	if [ "$list2" != "" ];then
		#Running
		echo "There have some created hadoop container."
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		docker ps -a | grep -E "slave|master|secondarynamenode|dns"
		echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		echo ""
	else
		echo "No hadoop container exists."
	fi

	#Call makesymble function
	makeSymble
	#Call headinfo function
	headInfo
}

#SSH Configuration in the docker
function sshConf(){
	list="`docker ps | grep -E "slave|master|secondarynamenode|dns" | awk '{print $NF}'`" #Get the name of hadoop container
	for container in $list
	do
		container_ip=$(docker inspect $container | grep IPAddress | cut -f4 -d '"')
		known_hosts="$container,$container_ip"
		known_hosts=$known_hosts" ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNhSjuhiLxYqNBQPnwUKQJlPfs/lqHPGwMxcT5D9saXXZ6gb75f22Yn1ClRmktzh29vOziEMCMgm3iOiQ/UOdak="
		echo $known_hosts >> $known_hosts_path
	done
}

#Namenode Configuration
function namenodeSlaveConf(){
	echo "`docker ps | grep 'slave' | awk '{print $NF}'`" > $hadoop_slaves_path
}

#Spark Slaves
function sparkSlaveConf(){
	echo "`docker ps | grep 'slave' | awk '{print $NF}'`" > $spark_slaves_path
}

#Make Symble Start
function makeSymble(){
	for ((i=1;i<=2;i++))
	do
		echo ""
	done
	echo "-----------------------------------------------------------------------"
}

#Run Hadoop Container
function runContainer(){
	rootness
	isDocker
	pathEnvironment
	startDocker
	startContainer
	namenodeSlaveConf
	sparkSlaveConf
	sshConf
	restartdns
	enterHadoop
}

#Show Result of Installation
function resultInfo(){
	echo ""
	echo "*******************************************************************************************"
	echo "*******************************************************************************************"
	echo "Congradulations! Hadoop Cluster has been Built and Insltalled successfully. "
	echo "*******************************************************************************************"
	echo "*******************************************************************************************"
	echo ""
}

#The Header Information
function headInfo(){
	echo "This shell script will build hadoop cluster based on the virtulization of docker:"
	echo ""
	echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Notice!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	echo "There maybe have some container you have ever created.And you should "
	echo "clear and remove them before build new container."
	echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Notice!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

	#Call makesymble function
	makeSymble

	echo "1. Clear and Remove Hadoop Container What have been created!"
	echo "2. Build Hadoop Cluster Using Docker. "
	echo "3. Look up created or running Hadoop Container."
	echo "Others to Exit. "
	echo "Please input the number:"
	read num
	case "${num}" in 
	[1] ) (resetDocker);;
	[2] ) (runContainer);;
	[3] ) (checkContainer);;
	 *  ) echo "Nothing you will do.";;
	esac
}
headInfo
