#! /bin/bash
rm -rf {mvcmd,quotation,sourcefile,newfile,swapfile1,swapfile2,swapfile3,movefile.sh,suffix}

touch {mvcmd,quotation,sourcefile,newfile,swapfile1,swapfile2,swapfile3,movefile.sh,suffix}

ls *.ape >> sourcefile
lines=`wc -l sourcefile | awk -F ' ' '{print $1}'`
ls *.ape | awk -F '[-.]' '{print $2}' >> newfile

for (( i=1;i<=$lines; i++ ))
	do
		echo "mv" >> mvcmd
		echo '"' >> quotation
		echo ".ape" >> suffix
	done

echo "#! /bin/bash" >> movefile.sh
echo "echo 'The renaming file procedure is starting...'"
paste -d '' quotation sourcefile quotation >> swapfile1
paste -d '' quotation newfile quotation >> swapfile2
paste -d ' ' mvcmd swapfile1 swapfile2 >> swapfile3
paste -d '' swapfile3 suffix > movefile.sh
sed -i 's/ ".ape/".ape/g' movefile.sh
echo "echo 'All files have been renamed successfully! '" >> movefile.sh
chmod a+x movefile.sh
./movefile.sh
rm -rf {mvcmd,quotation,sourcefile,newfile,swapfile1,swapfile2,swapfile3,movefile.sh,suffix}
