# Opens the first few search results for the keywords entered in command line on Google.
import sys, requests, webbrowser, bs4
#from bs4 import BeautifulSoup

print('Googling..')
res = requests.get('https://www.google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')
numopen = min(5, len(linkElems))
for i in range(numopen):
	webbrowser.open('https://www.google.com/search?q=' + linkElems[i].get('href'))