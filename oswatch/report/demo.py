#!/usr/bin/python
#coding:utf-8

#Function:Auto generate reports for Oracle Server based on latex file
#Description:
#Author:Abelit
#Email:ychenid@live.com
#Date:2016-04-11
import os
import file_handler
# file_handler.file_handler(infile='oswatch.tex',outfile='osreport.tex')

f1=file_handler.FileHandler(infile='oswatch.tex',outfile='osreport.tex')
f1.writer()