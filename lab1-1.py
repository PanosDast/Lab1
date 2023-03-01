import requests  # εισαγωγή της βιβλιοθήκης

url = input('Enter url:')   # προσδιορισμός του url

with requests.head(url) as response:  # το αντικείμενο response
	print(response.headers)

input("Press Enter to continue...")
