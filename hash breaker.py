#Hash breaker 
import requests
import re
import hashlib
import itertools

def create_dict_with_hash():
	dict = {}
	for x in itertools.permutations('0123456789', 4):
		key = ''.join(x)
		hash_value = hashlib.sha1(key.encode())
		dict[key] = hash_value.hexdigest()
	return dict

login_url = 'https://ringzer0ctf.com/login'
challenge_url = 'https://ringzer0ctf.com/challenges/56'
hashTxt = '\r\n\t\t----- BEGIN HASH -----<br />\r\n\t\t(.*)<br />\r\n\t\t'
flag = 'FLAG-(\w+)'
dictionary = create_dict_with_hash()

post_data = {'username': 'USER_HERE','password':'PASSWORD_HERE'}
session = requests.session()
session.post(login_url, data=post_data)
r = session.post(challenge_url)
#HASH HERE!
body = re.search(hashTxt, r.text).group(1)
result=''
for key,value in dictionary.items():
	if(value == body):
		result = key

r = session.post(challenge_url+'/'+str(result))
rtaFlag = re.search(flag,r.text).group(1)
if rtaFlag:
	print('FLAG-'+rtaFlag)
else:
	print('Something went wrong :( ')
