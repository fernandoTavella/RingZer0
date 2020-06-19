import base64
import string 
import requests
import re
from itertools import cycle

login_url = 'https://ringzer0ctf.com/login'
challenge_url = 'https://ringzer0ctf.com/challenges/16'
xorRe = '----- BEGIN XOR KEY -----<br />\r\n\t\t(.*)<br />'
messageRe = '----- BEGIN CRYPTED MESSAGE -----<br />\r\n\t\t(.*)<br />'
flagRe='FLAG-(.*)</div>'
xorKey = ''
messageClean = ''
keySize = 10
def xor_strings(message, key):
	return ''.join(chr(ord(c)^ord(k)) for c,k in zip(message, cycle(key)))
	       
def findMessage(xorKey,cryptedMessage):
	for i in range(0,len(xorKey)-keySize):
		possible=xorKey[i:10+i]
		message = xor_strings(cryptedMessage,possible)
		if all(x.islower() or x.isupper() or x.isdigit() for x in message):		
			return message
		i+=1

session = requests.session()
session.post(login_url, data={'username':'USER_HERE','password':'PASSWORD_HERE'})
r = session.post(challenge_url)
xorKey = re.search(xorRe, r.text).group(1)
messageClean = base64.b64decode(re.search(messageRe, r.text).group(1)).decode('utf-8')
areYou = findMessage(xorKey,messageClean)
r = session.post(challenge_url+'/'+areYou)
print('FLAG-'+re.search(flagRe, r.text).group(1))
