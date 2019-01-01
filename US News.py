import requests
from bs4 import BeautifulSoup
import csv
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Pragma':'no-cache','Referer':'https://www.usnews.com','Cache-Control':'no-cache','Accept-Language':'en-us','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15','Accept-Encoding':'br, gzip, deflate','Connection':'keep-alive'}
links,names,ranks,tuition,enrollment,city,state = [],[],[],[],[],[],[]
def crawl(url):
    req = requests.get(url,headers=headers)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    for link in soup.find_all("h3","heading-large block-tighter"):
        link=link.find("a")
        links.append("https://www.usnews.com"+link.get("href"))
        names.append(link.text)
    for link in soup.find_all("p","display-block block-flush text-strong"):
        ranks.append(link.get_text().strip())
    for link in soup.find_all("div","display-inline-for-medium-up inline-right-tight-for-medium-up border-right-for-medium-up"):
        if (link.find("span").text=='Tuition and Fees'):
            tuition.append(link.find("strong").text)
        else:
            enrollment.append(link.find("strong").text)
    for link in soup.find_all("p","display-block block-normal text-small"):
        t=link.get_text().strip()
        city.append(t[:t.find(',')])
        state.append(t[t.find(',')+2:])
for x in range(1,31):
    url=("https://www.usnews.com/best-colleges/rankings/national-universities?_page="+str(x))
    crawl(url)
big=[links,names,ranks,tuition,enrollment,city,state]
big=list(map(list, zip(*big)))
with open('USNewsRankings.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(big)