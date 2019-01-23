import requests,urllib
from bs4 import BeautifulSoup
import csv
import re
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Pragma':'no-cache','Referer':'https://www.usnews.com','Cache-Control':'no-cache','Accept-Language':'en-us','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15','Accept-Encoding':'br, gzip, deflate','Connection':'keep-alive'}
names,ranks,tuition,enrollment,city,state,tYpe,gender,year,religion,setting,endowment,international,usnews = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
temp1,temp2=[],[]
def crawl(url,web):
    req = requests.get(url,headers=headers)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    if web == "USNews":
        for link in soup.find_all("h3","heading-large block-tighter"):
            link=link.find("a")
            usnews.append("https://www.usnews.com"+link.get("href"))
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
    if web == "USNewsStats":
        stats=[]
        for link in soup.find_all("p","block-normal"):
            t=link.get_text()
            result=re.search(r'founded in (\S+)', t)
            if result:
                year.append(result.group(0)[11:15])
        for link in soup.find_all("span","heading-small text-black text-tight block-flush display-block-for-large-up"):
            t=link.get_text()
            stats.append(t)
        tYpe.append(stats[0][:stats[0].find(',')])
        gender.append(stats[0][stats[0].find(',')+2:])
        year.append(stats[1])
        religion.append(stats[2])
        setting.append(stats[4])
        endowment.append(stats[5])
    if web == "International%":
        for table in soup.find_all("tr"):
            if len(table.find_all("td")) == 3:
                temp1.append(table.find_all("td")[0].get_text().strip())
                temp2.append(table.find_all("td")[2].text)

for x in range(1,31):
    url=("https://www.usnews.com/best-colleges/rankings/national-universities?_page="+str(x))
    crawl(url,"USNews")
for i in usnews:
    crawl(i,"USNewsStats")
for i in range(1,28):
    url=("https://www.usnews.com/best-colleges/rankings/national-universities/most-international?_page="+str(i))
    crawl(url,"International%")
for name in names:
    for i in range(len(temp1)):
        if temp1[i] == name:
            international.append(temp2[i])
            break
        elif i == len(temp1)-1:
            international.append("DNE")

big=[names,ranks,tuition,enrollment,city,state,tYpe,gender,year,religion,setting,endowment,international,usnews]
big=list(map(list, zip(*big)))
with open('USNewsRankings.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Name","US News Raking","Tuition","Enrollment","City","State","School Type","Gender","# Years","Religious Affiliation","Setting","Endowment","International %"])
    writer.writerows(big)
