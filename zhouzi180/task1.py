
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

        ChkCoderesp = requests.get(ChkCodeurl)
        ChkCode = re.search('(?<=ChkCode=).{4}',ChkCoderesp.cookies['validateCookie']).group(0)
        post_data = {
            '__LASTFOCUS':'',
            '__VIEWSTATE':'/wEPDwUKMTIyMDg1NDMxNGRkWqLP0CWZLUdRH3hlV0v6WL0OoKVWTnjLKYdxAUqfTV8=',
            '__EVENTTARGET':'',
            '_EVENTARGUMENT':'',
            'Txt_UserName':self.username,
            'Txt_PassWord':self.password,
            'Txt_Yzm':ChkCode,
            'Btn_login':''
        }#data少了前4行，之前就报错非法登录
        self.cookies =ChkCoderesp.cookies
        post_response = requests.post(Baseurl,
                                      headers=self.headers,
                                      cookies=self.cookies,
                                      data=post_data)


    def get_page(self):
        """Get user index page."""
        self.login()
        response = requests.get("http://222.204.3.49:8082/user/Index.aspx", cookies=self.cookies)
        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        return response.text
