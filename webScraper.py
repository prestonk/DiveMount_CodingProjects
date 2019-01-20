import urllib2
from bs4 import BeautifulSoup



list = []

for a in range(41):
    page = "http://diveadvisor.com/united-states/dive-shops/page"+str(a)
    site = urllib2.urlopen(page)
    soup = BeautifulSoup(site)
    test = soup.findAll('h2', title=True)
    for c in test:
         list.append(c['title'])

print list
with open('test.txt', 'w') as f:
    for item in list:
        f.write("%s\n" % item)
