#! /bin/bash
echo "Please input old string which will be replaced by  a new string that you want to do.):"
read oldString
echo "Please input new string:"
read newString
#filePath=`pwd`
for file in `grep $oldString -r . | awk -F ':' '{print $1}'` 
do
	sed -i s/$oldString/$newString/g $file
done	
