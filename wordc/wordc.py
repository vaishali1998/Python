import requests

url = raw_input("Enter URL: ")

send = requests.get(url)

data1 = send.text

data = data1.lower()

print("Type 'exit' to exit program")
i=1
while(i):
	word = raw_input("Enter word to be count: ")
	count = data.count(word)
	print("Occurrence of the word:" +str(count))

	if word == 'exit':
		i=0
