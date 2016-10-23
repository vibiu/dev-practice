"""Task1."""
import re
import requests
url = 'http://222.204.3.49:8082'


class _LoginUser():
    """Login user class, for pass the test."""

    def __init__(self, username, password):
        """:param id: user id."""
        self.username = username
        self.password = password
        self.sessionid, self.view_state = self.get_session()
        self.chkcode = self.get_chkcode()
        self.islogin = self.login()
        if not self.islogin:
            raise ValueError('login fail')

    def get_session(self):
        """Get ASP.NET session id from the first get of main page."""
        resp = requests.get(url)
        asp_session = resp.cookies.get('ASP.NET_SessionId')
        pattern = re.compile('id="__VIEWSTATE" value="/(\w+?)="')
        match = pattern.search(resp.text)
        if match:
            view_state = '%2F' + match.groups()[0] + '%3D'
        else:
            view_state = ''
            raise ValueError('re not matched')
        return (asp_session, view_state)

    def get(self, prefix):
        """Get method wrapper.

        :param prefix: url prefix without host.
        """
        absurl = url + '/' + prefix if prefix else url
        resp = requests.get(
            absurl, cookies={'ASP.NET_SessionId': self.sessionid})
        return resp

    def post(self, prefix, data, allow_redirects=True):
        """Post method wrapper.

        :param prefix: url prefix without host.
        :param data: post body data.
        :allow_redirects: whether auto redirect is allowed, default True.
        """
        absurl = url + '/' + prefix if prefix else url
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ASP.NET_SessionId={}; validateCookie=ChkCode={}'.format(
                self.sessionid, self.chkcode),
        }
        resp = requests.post(
            absurl, headers=headers, data=data, allow_redirects=allow_redirects
        )
        return resp

    def get_chkcode(self):
        """Get check code from check code cookie."""
        prefix = 'gif.aspx?'
        resp = self.get(prefix)
        chkcode = resp.headers.get('Set-Cookie').split(';')[0].split('=')[-1]
        return chkcode

    def login(self):
        """Let user login first."""
        data = '__VIEWSTATE={}&Txt_UserName={}&Txt_PassWord={}'\
            '&Txt_Yzm={}&Btn_login='.format(
                self.view_state, self.username, self.password, self.chkcode)
        resp = self.post('/', data=data, allow_redirects=False)
        if resp.status_code == 302:
            return True
        return False

    def get_page(self):
        """Get user index page."""
        resp = self.get('user/Index.aspx')
        return resp.text
