import requests
from bs4 import BeautifulSoup

def main():
    baseurl="http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&sortid=164&%1=&sortid=164&page=2"
    r=requests.get(baseurl)
    soup=BeautifulSoup(r.text)
    content=soup.find_all("div",class_="bm_c")
    the_url_list=content.find_all("a")
    url_list=set
    for url in the_url_list:
        if ""
