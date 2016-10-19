import gevent.monkey
gevent.monkey.patch_all()
import gevent
import requests
from bs4 import BeautifulSoup
from spider import DataSpider,CommentSpider
from db import UserProfile,Comment

def fetchProfile(url):
    dat=DataSpider(url)
    dat.sendRequest()

def crawlComment(url):
    dat=CommentSpider(url)
    dat.sendRequest()

def fetchComment(urlele):
    print urlele
    greenlets=[]
    for i in range(1,urlele[1]/20+2):
        greenlets.append(gevent.spawn(crawlComment(urlele[0]+"&page="+str(i))))
    gevent.joinall(greenlets)


def main():
    UserProfile.drop_collection()
    baseurl="http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&sortid=164&%1=&sortid=164&page="

    for i in range(1,3):
        r=requests.get(baseurl+str(i))
        soup=BeautifulSoup(r.text)
        url_list=soup.find_all("a",class_="s xst")
        greenlets=[]
        for url in url_list:
            greenlets.append(gevent.spawn(fetchProfile(url.attrs['href'])))
        gevent.joinall(greenlets)
        print "done,{}/{}".format(i,938)

def getComment():
    Comment.drop_collection()
    baseurl="http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=28&sortid=192&filter=sortid&sortid=192&page="
    for i in range(1,142):
        r=requests.get(baseurl+str(i))
        soup=BeautifulSoup(r.text)
        table=soup.find_all("table",summary="forum_28")[0]
        for tbody in table.find_all("tbody")[1:]:
            url=a=tbody.find_all("a",class_="s xst")[0].attrs['href']
            td=tbody.find_all("td",class_="num")[0]
            num=int(td.a.text)
            fetchComment((url,num))
    print "done,{}/{}".format(i,142)

if __name__=="__main__":
    getComment()
