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

def make_form(rows,cols,text_width,text_height):   #define the funcion that how to make form
    for i in range(rows):
        print('+'+('-'*text_width+'+')*cols)
        for j in range(text_height):
            print('|'+(' '*text_width+'|')*cols)
    print('+'+('-'*text_width+'+')*cols)
    
def customize_form():    #define customized function
    rows_input=int(input("Please enter the rows of form:"))
    cols_input=int(input("Please enter the cols of form:"))
    text_w=int(input("Please enter the width of text:"))
    text_h=int(input("Please enter the height of text:"))

    make_form(rows_input,cols_input,text_w,text_h)  #call function make_form()
    
def default_form():
    rows_input=4
    cols_input=5
    text_w=10
    text_h=3
    
    make_form(rows_input,cols_input,text_w,text_h)
    
def random_form(): #define form function by system random
    rows_input=random.randrange(31) #takes a random number from 0 to 30
    cols_input=random.randrange(31)
    text_w=random.randrange(5,16,1) #takes a random number from 5 to 15
    text_h=random.randrange(1,5,1)

    make_form(rows_input,cols_input,text_w,text_h)
    
print('='*80)
print("Welcome to use this function! This procedure is used for making form running based on python3+.\nNote:\n1.You can use it to make defalt form 5 by 5;\n2.And you can make form as your customizitons.\n3.Others you can make form as system defined by random.\nIf you have any question,please contact ychenid@live.com.")
print('Author:ChenYing\n'+'Time:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*80)

def my_form():
    print("Please choose the method to make form, 1 means making form by default,2 means making form by customized and 3 means making form by system random.")
    choose=input("Please choose a number between 1(default) , 2(customized) or 3(random):")
    if choose=='1' or choose=='default':
        choose='1'
    if choose=='2' or choose=='customized':
        choose='2'
    if choose=='3' or choose=='random':
        choose='3'
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
            my_form()
    else:
        print()
        print('*'*30+'This is a new line'+'*'*30)
        my_form()
        
my_form()
