import requests
from bs4 import BeautifulSoup


class DataSpider():
    def __init__(self,url):
        self.url=url
        self.Header={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7"
        }

    def sendRequest(self):
        resp=requests.get(self.url,headers=self.Header)
        soup=BeautifulSoup(resp.text)
        self.content=soup.find_all("div",class_="pct")[0].div
        self.leave_time=self.content.u.span.find_all("span")[0].text[1:]
        self.wanna_diploma=self.content.u.span.find_all("span")[1].text
        self.result=self.content.u.span.find_all("span")[2].text
        self.wanna_subject=self.content.u.span.find_all("span")[3].text
        self.wanna_university=self.content.u.span.find_all("b")[2].text

        string=self.content.find_all("li")[1].text.strip()
        self.undergraduate_subject=""
        start=False
        for i in string:
            if i=="@":
                break
            if start:
                self.undergraduate_subject+=i
            if i==":":
                start=True
        self.undergraduate_university=""
        start=False
        for i in string:
            if i==",":
                break
            if start:
                self.undergraduate_university+=i
            if i=="@":
                start=True
        self.undergraduate_GPA=""
        start=False
        for i in string:
            if i==":":
                break
            if start:
                self.undergraduate_GPA+=i
            if i==",":
                start=True
        string=self.content.find_all("li")[2].text.strip()
        self.ms_subject=""
        start=False
        for i in string:
            if i=="@":
                break
            if start:
                self.ms_subject+=i
            if i==":":
                start=True
        self.ms_university=""
        start=False
        for i in string:
            if i==",":
                break
            if start:
                self.ms_university+=i
            if i=="@":
                start=True
        self.ms_GPA=""
        start=False
        for i in string:
            if i==":":
                break
            if start:
                self.ms_GPA+=i
            if i==",":
                start=True
        string=self.content.find_all("li")[3].text.strip()
        self.toefl=""
        start=False
        for i in string:
            if start:
                self.toefl+=i
            if i==":":
                start=True
        string=self.content.find_all("li")[4].text.strip()
        self.GRE=""
        start=False
        for i in string:
            if start:
                self.GRE+=i
            if i==":":
                start=True
        string=self.content.find_all("li")[6].text.strip()
        start=False
        self.something=""
        for i in string:
            if start:
                self.something+=i
            if i==":":
                start=True
