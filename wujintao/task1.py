
#!uer/bin/python3.5
#coding:utf-8
"""Task1."""
from urllib import request
from bs4 import BeautifulSoup
import requests
import http.cookiejar
import re

url = 'http://222.204.3.49:8082'
url2 = r"http://222.204.3.49:8082/gif.aspx"

class LoginUser():
    """Login user class, for pass the test."""

    def __init__(self, username, password):
        """Initlize username and password."""
        self.username = username
        self.password = password

    def ask_cookie(self,url):
        """get cookies from urls."""
        cookie = http.cookiejar.CookieJar()
        #  to save cookie object
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        responser = opener.open(url)
        return cookie

    def login(self):
        """User login."""
        list1 = []
        # to save the Verification Code.
        """to get the Verification Code."""
        Cookies = self.ask_cookie(url2)
        for i in Cookies:
            list1.append(i.value)
        resu = re.findall(r".*=(.*)", list1[1])
        Yzm = resu[0]
        # get the code.
        data = {
            '__VIEWSTATE': "/wEPDwUKMTIyMDg1NDMxNGRkWqLP0CWZLUdRH3hlV0v6WL0OoKVWTnjLKYdxAUqfTV8=",
            'Txt_UserName': self.username,
            'Txt_PassWord': self.password,
            'Txt_Yzm': Yzm,
            'Btn_login': ''
        }
        # get the form

        html = requests.post(url, data=data, cookies=Cookies)
        # care the method.
        return (html.text)

    def get_page(self):
        """Get user index page."""
        str1 = self.login()
        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        aim = ''
        soup = BeautifulSoup(str1)
        td_tag = soup.find_all(name='td',attrs={'colspan': 2, 'height': 31, 'align': 'left'})
        aim = re.findall(r".*?l\>(.+?)\<f.*$",str(td_tag),re.S)
        aim = aim[0]
        print(aim)
        return aim
