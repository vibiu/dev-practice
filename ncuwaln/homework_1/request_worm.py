import re
from urllib import request, parse
from http import cookiejar


url = "http://222.204.3.49:8082/"


Txt_UserName = "8000115110"
Txt_PassWord = "8000115110"
Txt_Yzm = ""
cookies = cookiejar.LWPCookieJar()
handler = request.HTTPCookieProcessor(cookies)
opener = request.build_opener(handler)
with opener.open(url+"gif.aspx?") as html:
    for cookie in cookies:
        if cookie.name == "validateCookie":
            Txt_Yzm = re.match(r"ChkCode=([1234567890qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYYHNUJMIKLOP]*)", cookie.value).group(1)
data = {
    'Btn_login': '',
    "Txt_UserName": Txt_UserName,
    "Txt_PassWord": Txt_PassWord,
    "Txt_Yzm": Txt_Yzm,
    "__ViEWSTATE": "/wEPDwUKMTIyMDg1NDMxNGRkWqLP0CWZLUdRH3hlV0v6WL0OoKVWTnjLKYdxAUqfTV8="
}
def get_page():
    post_data = parse.urlencode(data).encode()
    req = request.Request(url, post_data)
    print(req.get_method())
    with opener.open(req) as f:
        return f.read().decode("gbk")
