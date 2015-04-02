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
def make_form(rows,cols,text_width,text_height):
    for i in range(rows):
        print('+'+('-'*text_width+'+')*cols)
        for j in range(text_height):
            print('|'+(' '*text_width+'|')*cols)
    print('+'+('-'*text_width+'+')*cols)
    
def customize_form():    
    rows_input=int(input("Please enter the rows of form:"))
    cols_input=int(input("Please enter the cols of form:"))
    text_w=int(input("Please enter the width of text:"))
    text_h=int(input("Please enter the height of text:"))

    make_form(rows_input,cols_input,text_w,text_h)
    
def default_form():
    rows_input=4
    cols_input=5
    text_w=10
    text_h=3
    make_form(rows_input,cols_input,text_w,text_h)
    
print('='*80)
print("Welcome to use this function! This procedure is used for making form running based on python3+.\nNote:\nYou can use it to make defalt form 5 by 5;\nAnd also you can make form as you defined.\nIf you have any question,please contact ychenid@live.com.")
print('='*80)

def my_form():
    print("Please choose the method to make form, 1 means making form by default and 2 means making form by customized.")
    choose=input("Please choose a number between 1(default) and 2(customized):")
    if choose=='1' or choose=='default':
        choose='1'
    if choose=='2' or choose=='customized':
        choose='2'
   
    if (choose).isdigit():
        if choose=='1':
            default_form()
        elif choose=='2':
            customize_form()
        else:
            print("The number you entered can not match the tips.")
            my_form()
    else:
        my_form()
        
my_form()
