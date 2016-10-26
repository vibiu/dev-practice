
"""Task1."""
import re
import requests

Baseurl = 'http://222.204.3.49:8082'
ChkCodeurl = 'http://222.204.3.49:8082/gif.aspx?'

class LoginUser():
    """Login user class, for pass the test."""

    def __init__(self, username, password):
        """Initlize username and password."""
        self.username = username
        self.password = password
        self.cookies = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://222.204.3.49:8082',
            'Referer': 'http://222.204.3.49:8082/'
        }


    def login(self):
        """User login."""
        get_response = requests.get(Baseurl)
        request_cookies = get_response.cookies
        ChkCoderesp = requests.get(ChkCodeurl)
        ChkCode = re.search('[0-9A-Z]{4}',ChkCoderesp.cookies['validateCookie']).group(0)
        post_data = {
            'Txt_UserName': self.username,
            'Txt_PassWord': self.password,
            'Txt_Yzm': ChkCode,
            'Btn_login': ''
        }
        post_response = requests.post(Baseurl,
                                      headers=self.headers,
                                      cookies=request_cookies,
                                      data=post_data)
        self.cookies =request_cookies

    def get_page(self):
        """Get user index page."""
        self.login()
        response = requests.get("http://222.204.3.49:8082/user/Index.aspx", cookies=self.cookies)
        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        return response.text