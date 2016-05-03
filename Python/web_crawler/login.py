import urllib,re,os
import urllib.request as urllib2
import http.cookiejar as cookielib
import sqlite3,time
def LoginBaiDu(user,pwd):
         
        #设置
        cookie = cookielib.CookieJar()
        cookieProc = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookieProc)
        urllib2.install_opener(opener)
 
        #请求
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2'}
        post = {
            'username':user,
            'password':pwd,
            'tpl':'mn',
            'u':'http://www.baidu.com/',
            'psp_tt':0,
            'mem_pass':'on'
            }
        post = urllib.parse.urlencode(post)
        post = post.encode('utf-8')
        req = urllib2.Request(
            url='https://passport.baidu.com/?login',
            data=post,
            headers = header
            )
        res = urllib2.urlopen(req).read(500)
         
        if 'passCookie' in res:
            flag = True
         
        else:
            flag = 'Login Fail:%s'%user
             
        return flag
        print (flag)
         
    #sb = SpiderBaiDu()
if __name__ == '__main__':
    LoginBaiDu('ychenid@live.com','yingchen')

    
# For a script working with Python 2 (tested versions 2.7.3 and 2.6.8) and Python 3 (3.2.3 and 3.3.2+) try:

# #! /usr/bin/env python

# try:
#     # For Python 3.0 and later
#     from urllib.request import urlopen
# except ImportError:
#     # Fall back to Python 2's urllib2
#     from urllib2 import urlopen

# html = urlopen("http://www.google.com/")
# print(html.read())