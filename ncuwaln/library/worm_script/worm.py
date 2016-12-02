import requests
from bs4 import BeautifulSoup
import pytesseract

class Worm(object):
    search_url = "http://210.35.251.243/opac/openlink.php"
    post_url = "http://210.35.251.243/reader/redr_verify.php"
    img_url = "http://210.35.251.243/reader/captcha.php"

    def __init__(self):
        self.data = {
            "select": "cert_no",
            "returnUrl": ""
        }

    def get_book_info(self, strText, strSearchType="title", displaypg=1000):
        data = {
            "strText": strText,
            "strSearchType": strSearchType,
            "displaypg": displaypg
        }
        response = requests.get(self.search_url, params=data)
        response.encoding = "utf-8"
        html = BeautifulSoup(response.text)
        i = 0;
        results = []
        for x in html.find_all(name="li", attrs={"class": "book_list_info"}):
            book_id = x.find_next(name="h3").find_next(name="a").string
            stock = x.find_next(name="p").find_next(name="br").string.replace("\n\r\t", "").strip()
            results.append({"book_id": book_id, "stock": stock})
        return results


    def login(self, username, password, cookie, image):
        self.data["number"] = username
        self.data["passwd"] = password
        # captcha = pytesseract.image_to_string(image)
        with open("test.gif", "wb") as w:
            w.write(image)
        captcha = input()
        self.data["captcha"] = captcha
        response = requests.post(self.post_url, data=self.data, cookies=cookie)
        response.encoding = "utf-8"
        return username in response.text

