import requests
import certifi
import re
from io import BytesIO
from urllib.parse import urlencode

login_url = 'https://ringzer0ctf.com/login'
challenge_url = 'https://ringzer0ctf.com/challenges/32'
begin = '----- BEGIN MESSAGE -----<br />\r\n\t\t(.*)<br />\r\n\t\t----- END MESSAGE -----<br />\r\n\t\t'
flag = 'FLAG-(\w+)'
post_data = {'username': 'USER_HERE','password':'PASSWORD_HERE'}
session = requests.session()
session.post(login_url, data=post_data)
r = session.post(challenge_url)

#DECIMAL + HEXA - BINARY = ANSWER
body = re.search(begin, r.text).group(1)
# 0 = HEXA | 1 = DEC | 2 = BIN
values = re.findall(r'0x[0-9A-F]+', body, re.I) + [int(s) for s in body.split() if s.isdigit()]
result = values[1] + int(values[0], 0) -int(str(values[2]), 2)
r = session.post(challenge_url+'/'+str(result))
rtaFlag = re.search(flag,r.text).group(1)
if rtaFlag:
	print('FLAG-'+rtaFlag)
else:
	print('Something went wrong :( ')
