Filename mymail email "ychenid@live.com"; 
Data _null_; 
file mymail 
to=("948640709@qq.com") /*????*/ 
subject="My SAS output" /*??*/ 
attach=("C:\Users\Ying\Desktop\sid.txt"); /*??*/ 
put "i love sas"; /*????*/ 
put "yes it's true"; 
run;
