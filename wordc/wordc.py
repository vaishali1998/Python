print("                                                     o        o__ __o   ")
print("                                                    <|>      /v     v\  ")
print("                                                    < \     />       <\ ")
print("  o              o     o__ __o    \o__ __o     o__ __o/   o/            ")
print(" <|>            <|>   /v     v\    |     |>   /v     |   <|             ")
print(" < >            < >  />       <\  / \   < >  />     / \   \\            ")
print("  \o    o/\o    o/   \         /  \o/        \      \o/     \         / ")
print("   v\  /v  v\  /v     o       o    |          o      |       o       o  ")
print("    <\/>    <\/>      <\__ __/>   / \         <\__  / \      <\__ __/>  ")
print("\n")
print("A Simple Python Code to count number of words in any web page") 
print("\n")

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
	print("Occurrence of the word "+word+": "+str(count))

	if word == 'exit':
		i=0

