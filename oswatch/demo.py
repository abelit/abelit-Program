#!/usr/bin/python
#coding:utf-8

#Function:Auto generate reports for Oracle Server based on latex file
#Description:
#Author:Abelit
#Email:ychenid@live.com
#Date:2016-04-11
import os
import file_handler
import osinfo

# file_handler.file_handler(infile='oswatch.tex',outfile='osreport.tex')

f1=file_handler.FileHandler('oswatch.tex','osreport.tex')
f1.writer()




cpuinfo=osinfo.cpu_stat()
diskinfo=osinfo.disk_stat()
print(cpuinfo[0]['model name'])
print(diskinfo)
