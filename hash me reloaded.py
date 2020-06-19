#Hash me again
import hashlib
import requests
import re

login_url = 'https://ringzer0ctf.com/login'
challenge_url = 'https://ringzer0ctf.com/challenges/14'
begin = '----- BEGIN MESSAGE -----<br />\r\n\t\t(.*)<br />\r\n\t\t----- END MESSAGE -----<br />'
flag = 'FLAG-(\w+)'

session = requests.session()
session.post(login_url, data={'username':'USER_HERE','password':'PASSWORD_HERE'})
r = session.post(challenge_url)

body = re.search(begin, r.text).group(1)
message = ''.join(chr(int(body[i*8:i*8+8],2)) for i in range(len(body)//8))
hashed = hashlib.sha512(message.encode('utf-8')).hexdigest()
r = session.post(challenge_url+'/'+hashed)
rtaFlag = re.search(flag,r.text).group(1)
if rtaFlag:
	print('FLAG-'+rtaFlag)
else:
	print('Something went wrong :( ')