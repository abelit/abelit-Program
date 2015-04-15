#!/bin/bash python
##screen_width=101
##box_total_width=81
##box_each_width=10
##left_margin=(screen_width-box_total_width)//2
##print()
##print(' '*left_margin+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+')
##print(' '*left_margin+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|')
##print(' '*left_margin+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|')
##print(' '*left_margin+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+')
##print(' '*left_margin+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|')
##print(' '*left_margin+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|')
##print(' '*left_margin+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+')
##print(' '*left_margin+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|')
##print(' '*left_margin+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|'+' '*box_each_width+'|')
##print(' '*left_margin+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+'+'-'*box_each_width+'+')
##print()

##----------------------
##function:make form as definded by custom
##----------------------
import random #includes module
import time
from datetime import date

def make_form(table_title,table_unit,rows,cols,text_width,text_height):   #define the funcion that how to make form
    table_title_width=len(table_title)
    table_unit_width=len(table_unit)
    table_width=text_width*cols+cols+1
    print()
    print(' '*((table_width-table_title_width)//2)+table_title+' '*(((table_width-table_title_width)//2)-table_unit_width-1)+table_unit)
    print()
    for i in range(rows):
        print('+'+('-'*text_width+'+')*cols)
        for j in range(text_height):
            print('|'+(' '*text_width+'|')*cols)
    print('+'+('-'*text_width+'+')*cols)
    
def customize_form():    #define customized function
    rows_input=int(input("Please enter the rows of form:"))
    cols_input=int(input("Please enter the cols of form:"))
    text_width_input=int(input("Please enter the width of text:"))
    text_height_input=int(input("Please enter the height of text:"))
    table_title_input=input("Please enter the title of table:")
    table_unit_input=input("Please enter the unit of table:")
    make_form(table_title_input,table_unit_input,rows_input,cols_input,text_width_input,text_height_input)  #call function make_form()
    
def default_form():
    rows_input=4
    cols_input=5
    text_width_input=10
    text_height_input=3
    table_title_input="Table Example1:XXX"
    table_unit_input="Unit:xxx"
    make_form(table_title_input,table_unit_input,rows_input,cols_input,text_width_input,text_height_input)
    
def random_form(): #define form function by system random
    rows_input=random.randrange(1,11) #takes a random number from 1 to 11
    cols_input=random.randrange(1,11)
    text_width_input=random.randrange(5,16,1) #takes a random number from 5 to 15
    text_height_input=random.randrange(1,4,1)
    array_title=['How old are you?','Learning English','Learn Linux/Unix/Windows','Speaking Chinese','Watch TV','The menu of fruish','Sports Items']
    array_unit=['Unit:$']
    table_title_input='Table:'+random.choice(array_title)
    table_unit_input=random.choice(array_unit)
    make_form(table_title_input,table_unit_input,rows_input,cols_input,text_width_input,text_height_input)
    
print('='*80)
print("Welcome to use this function! This procedure is used for making form running based on python3+.\nNote:\n1.You can use it to make defalt form 5 by 5;\n2.And you can make form as your customizitons.\n3.Others you can make form as system defined by random.\nIf you have any question,please contact ychenid@live.com.")
print('Author:ChenYing\n'+'Time:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*80)

def exe_my_form():
    print("Please choose the method to make form, 1 means making form by default,2 means making form by customized and 3 means making form by system random.")
    choose=raw_input("Please choose a number between 1(default) , 2(customized) or 3(random),and 0(exit):")
    if choose=='1' or choose=='default':
        choose='1'
    if choose=='2' or choose=='customized':
        choose='2'
    if choose=='3' or choose=='random':
        choose='3'
    if choose=='0' or choose=='exit':
        print("You have exited successfully on "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    else:
        if (choose).isdigit(): #verify whether all data users entered is digit or not
            if choose=='1':
                default_form()
            elif choose=='2':
                customize_form()
            elif choose=='3':
                random_form()
            else:
                print()
                print('*'*30+'This is a new line'+'*'*30)
                print("The number you entered can not match the tips.")
                exe_my_form()
        else:
            print()
            print('*'*30+'This is a new line'+'*'*30)
            exe_my_form()
exe_my_form()
