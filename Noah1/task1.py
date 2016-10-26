"""Task1."""
import requests1
import re

url = r'http://222.204.3.49:8082'
posturl = r'http://222.204.3.49:8082/user/Index.aspx'
capthaurl = r'http://222.204.3.49:8082/gif.aspx?'

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
        capthadata = requests.get(capthaurl)
        captha = re.search('[0-9a-zA-Z]{4}$', capthadata.cookies['validateCookie']).group(0)
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
        postdata = {
            '__LASTFOCUS':'',
            '__VIEWSTATE':'/wEPDwUKMTIyMDg1NDMxNGRkWqLP0CWZLUdRH3hlV0v6WL0OoKVWTnjLKYdxAUqfTV8=',
            '__EVENTTARGET':'',
            '_EVENTARGUMENT':'',
            'Txt_UserName':self.username,
            'Txt_PassWord':self.password,
            'Txt_Yzm':captha,
            'Btn_login':''
        }
        self.cookies = requestcookies
        response = requests.post(url,headers = headers, cookies = self.cookies, data = postdata)
    def get_page(self):
        """Get user index page."""
        self.login()
        response = requests.get(posturl, cookies=self.cookies)
        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        return '【赖强】'


