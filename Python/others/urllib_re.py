
#urllib_re.py
from urllib import urlopen
import re

pattern=re.compile('<script src="(.*)"></script>')
url="http://www.yiibai.com/"
text=urlopen(url).read()    #.decode('UTF-8')
for contents in pattern.findall(text):
    print('%s' % contents)
###encoding:UTF-8
##import urllib.request
## 
##url = "http://www.baidu.com"
##data = urllib.request.urlopen(url).read()
##data = data.decode('UTF-8')
##print(data)
