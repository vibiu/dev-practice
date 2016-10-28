"""Task1."""

import requests
from bs4 import BeautifulSoup
import re

url = 'http://222.204.3.49:8082'
chk_code_url = "http://222.204.3.49:8082/gif.aspx?"


class LoginUser():
    """Login user class, for pass the test."""

    def __init__(self, username, password):
        """Initlize username and password."""
        self.username = username
        self.password = password
        self.cookies = None

    def login(self):
        """User login."""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html5lib")
        # get view state
        view_state = soup.select("#__VIEWSTATE")[0].attrs['value']

        cookies = {'validateCookie': "ChkCode=TYAN",
                   'ASP.NET_SessionId': response.cookies['ASP.NET_SessionId']}

        post_data = {
            '__VIEWSTATE': view_state,
            'Txt_UserName': self.username,
            'Txt_PassWord': self.password,
            'Txt_Yzm': "tyan",
            'Btn_login': ''
        }

        requests.post(url, cookies=cookies, data=post_data)

        self.cookies = cookies

    def get_page(self):
        """Get user index page."""
        self.login()
        response = requests.get("http://222.204.3.49:8082/user/Index.aspx", cookies=self.cookies)

        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        return response.text
