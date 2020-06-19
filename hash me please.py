#Hash me if you can
import requests
import re
import hashlib

session = requests.session()

login_url = 'https://ringzer0ctf.com/login'
challenge_url = 'https://ringzer0ctf.com/challenges/13'
begin = '----- BEGIN MESSAGE -----<br />\r\n\t\t(\w+)'
flag = 'FLAG-(\w+)'

session.post(login_url, data={'username':'USER_HERE','password':'PASSWORD_HERE'})
r = session.post(challenge_url)
value = re.search(begin, r.text).group(1)
hashed = hashlib.sha512(value.encode('utf-8')).hexdigest()
r = session.post(challenge_url+'/'+hashed)
rtaFlag = re.search(flag,r.text).group(1)
if rtaFlag:
	print('FLAG-'+rtaFlag)
else:
	print('Something went wrong :( ')