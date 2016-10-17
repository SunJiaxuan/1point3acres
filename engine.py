import gevent.monkey
gevent.monkey.patch_all()
import gevent
import requests
from bs4 import BeautifulSoup
from spider import DataSpider
from db import UserProfile

def fetchProfile(url):
    dat=DataSpider(url)
    dat.sendRequest()

def main():
    UserProfile.drop_collection()
    baseurl="http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&sortid=164&%1=&sortid=164&page="

    for i in range(1,938):
        r=requests.get(baseurl+str(i))
        soup=BeautifulSoup(r.text)
        url_list=soup.find_all("a",class_="s xst")
        greenlets=[]
        for url in url_list:
            greenlets.append(gevent.spawn(fetchProfile(url.attrs['href'])))
        gevent.joinall(greenlets)
        print "done,{}/{}".format(i,938)

if __name__=="__main__":
    main()
