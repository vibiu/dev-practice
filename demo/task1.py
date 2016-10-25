"""dev-practice demo.

author island
date 2016/10/25
power by py3.
"""

import re
import requests


class LoginUser(object):
    """Login user class."""

    def __init__(self, username, password):
        """Initialize."""

        self.username = username
        self.password = password
        self.url = 'http://222.204.3.49:8082/'

        # http request headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',  # make sure the data type of you send.
            'Origin': 'http://222.204.3.49:8082',
            'Referer': 'http://222.204.3.49:8082/'
        }

        # form data send by user
        self.form_data = {
            '__VIEWSTATE': '',
            'Txt_UserName': username,
            'Txt_PassWord': password,
            'Txt_Yzm': 'haha',  # verification code, just same as request cookie
            'Btn_login': '',
            '__LASTFOCUS': '',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': ''
        }

    def login(self):
        """Login."""

        # load login page in order to get the cookie named 'ASP.NET_SessionId'
        get_resp = requests.get(self.url)  # get method

        # before login the ASP.NET_SessionId is invalid 
        request_cookies = dict(get_resp.cookies)

        # cookie for verification code
        request_cookies['validateCookie'] = 'ChkCode=HAHA'

        # login, post method
        # after login, now the ASP.NET_SessionId was valid 
        post_resp = requests.post(self.url, headers=self.headers,
                    cookies=request_cookies, data=self.form_data)

        # return the respone
        return post_resp 

    def get_page(self):
        """Get index."""

        resp = self.login()  # get respone by login

        # filter the page by re
        match = re.search(r'BeautifulGreetings.*(【.*】)', resp.text)
        if match:
            return match.group(1)
        else:
            return 'failed'

