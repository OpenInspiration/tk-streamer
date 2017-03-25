from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://debatgemist.tweedekamer.nl')


bsObj = BeautifulSoup(html.read(), "lxml")


print (bsObj.h1)
print (bsObj.h2)
print (bsObj.h3)
print (bsObj.article)

print ('-------------------')

print (bsObj.span) ## <> Debat gemist <>
print(dir(bsObj.span))

print(bsObj.span.string) ## Debat Gemist
print(bsObj.span.contents) ## ['Debat Gemist']

print(bsObj.h2.string) ## Stemmingen
print(bsObj.h2.contents) ## ['Stemmingen']
