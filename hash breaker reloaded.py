# Hash breaker reloaded - SHA1
import pycurl
import certifi
import re
import hashlib
import itertools
from io import BytesIO
from urllib.parse import urlencode

login_url = 'https://ringzer0ctf.com/login'
challenge_url = 'https://ringzer0ctf.com/challenges/57'
begin = '\r\n\t\t----- BEGIN HASH -----<br />\r\n\t\t(.*)<br />\r\n\t\t'
salt = '\r\n\t\t----- BEGIN SALT -----<br />\r\n\t\t(.*)<br />\r\n\t\t'
flag = 'FLAG-(\w+)'

def breakHash(hashVal,saltVal,c):
	for key in range(1,10000):
			hash_value = hashlib.sha1((str(key)+saltVal).encode()).hexdigest()
			if(hash_value == hashVal):
				result = key
	if(result!=''):
		c.setopt(c.URL,challenge_url+'/'+str(result))
		c.setopt(c.WRITEFUNCTION, buffer.write)
		c.setopt(c.HEADERFUNCTION, header.write)
		c.perform()
		c.close()
		print('The flag is:')
		print(re.search(flag, buffer.getvalue().decode('UTF-8')).group(1))
	else:
		print('Not Found :(')

buffer = BytesIO()
header = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL,login_url)

post_data = {'username': 'USER_HERE','password':'PASSWORD_HERE'}
postfields = urlencode(post_data)
c.setopt(c.POSTFIELDS, postfields)
c.setopt(c.COOKIEFILE, '')	
c.setopt(c.CAINFO,certifi.where())
c.setopt(c.VERBOSE,True)
c.perform()
c.setopt(c.URL,challenge_url)
c.setopt(c.WRITEFUNCTION, buffer.write)
c.setopt(c.HEADERFUNCTION, header.write)
c.perform()

hashVal = re.search(begin, buffer.getvalue().decode('UTF-8')).group(1)
saltVal = re.search(salt, buffer.getvalue().decode('UTF-8')).group(1)
breakHash(hashVal,saltVal,c)