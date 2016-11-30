#!/usr/bin/python3
import requests
from PIL import Image
from pytesseract import image_to_string
from bs4 import BeautifulSoup
# import re

Basicurl = "http://opac.ncu.edu.cn/reader/redr_verify.php"
Chkurl = "http://opac.ncu.edu.cn/reader/captcha.php"


class LoginUser():
    """docstring for LO"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cookies = None
        self.headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://opac.ncu.edu.cn',
            'Referer': 'http://opac.ncu.edu.cn/opac/search.php',
            'Host': 'opac.ncu.edu.cn'
        }

    def get_capture(self):
        chk = requests.get(Chkurl)
        self.chkcookies = chk.cookies
        local = open(
            "./img_cache" + 'PHPSESSID' + ".gif", "wb")
        local.write(chk.content)
        local.close()
        gif = Image.open("./img_cache" + 'PHPSESSID' + ".gif")

        self.Chkcode = image_to_string(gif)

    def login(self):
        self.get_capture()
        post_data = {
            'number': '6103115112',
            'passwd': 'xiezhibin',
            'captcha': self.Chkcode,
            'select': 'cert_no',
            'returnUrl': ''
        }
        post_response = requests.post(Basicurl,
                                      headers=self.headers,
                                      cookies=self.chkcookies,
                                      data=post_data
                                      )
        # pattern = re.compile('')
        a = requests.get("http://opac.ncu.edu.cn/reader/book_lst.php",cookies = self.chkcookies)
        a.encoding = 'utf-8'
        soup = BeautifulSoup(a.text,"html5lib")
        b = soup.find_all("tr")
        for c in b:
            d = c.find_all("td")
            print d[].text
        # return a.text
        # print (self.chkcookies)
        # print (self.headers)


user = LoginUser('6130115112', 'xiezhibin')
page = user.login()
print(page)
