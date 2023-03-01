import requests  # εισαγωγή της βιβλιοθήκης
from datetime import datetime

url = input('Input url:')   # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
	print(response.headers)          # print headers
	print('Server software:', response.headers['server']) #print server software
	
	if response.cookies:      #check cookies
	    for c in response.cookies:  #print cookie names
		       print('Cookie:', c.name +"->", c.value)
		       if c.expires:        #print cookie expiry date
		           print('Cookie valid until:', datetime.fromtimestamp(c.expires))

input("Press Enter to continue...")
