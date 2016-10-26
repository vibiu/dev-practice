import requests
import re

url='http://222.204.3.49:8082'
captha_url='http://222.204.3.49:8082/git.aspx?'

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
    requestcookies = dict(response.cookies)
    captha_data = requests.get(captha_url)
    captha_ = re.search('\b[A-Z0-9]{4}\b',captha_data.cookies['validateCookie']).group(0)
    post_data = {
            '__VIEWSTATE': '/wEPDwUKMTIyMDg1NDMxNGRkWqLP0CWZLUdRH3hlV0v6WL0OoKVWTnjLKYdxAUqfTV8=',
            'Txt_UserName': self.username,
            'Txt_PassWord': self.password,
            'Txt_Yzm': captha_,
            'Btn_login': ''
        }
    headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Origin': 'http://222.204.3.49:8082',
            'Referer': 'http://222.204.3.49:8082/'
        }
            self.cookies = requestcookies
        response = requests.post(url,headers = headers, cookies = self.cookies, data = post_data)

         def get_page(self):
        """Get user index page."""
        self.login()
        response = requests.get(posturl, cookies=self.cookies)
        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        return response.text