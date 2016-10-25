
#!uer/bin/python3.5
#coding:utf-8
"""Task1."""
from urllib import request
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
        cookie = http.cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        responser = opener.open(url)
        return cookie

    def login(self):
        """User login."""
        list1 = []
        Cookies = self.ask_cookie(url2)
        for i in Cookies:
            list1.append(i.value)
        resu = re.findall(r".*=(.*)", list1[1])
        Yzm = resu[0]
        data = {
            '__VIEWSTATE': "/wEPDwUKMTIyMDg1NDMxNGRkWqLP0CWZLUdRH3hlV0v6WL0OoKVWTnjLKYdxAUqfTV8=",
            'Txt_UserName': self.username,
            'Txt_PassWord': self.password,
            'Txt_Yzm': Yzm,
            'Btn_login': ''
        }

        headers = requests.get(url, params=data, cookies=Cookies)
        print (headers.text)

    def get_page(self):
        """Get user index page."""
        self.login()
        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        return '【赖强】'
