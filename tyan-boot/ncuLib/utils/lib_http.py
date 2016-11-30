import requests
from bs4 import BeautifulSoup


def GetSoupWithPara(url, para):
    try:
        data = requests.get(url, para)
        data.encoding = "utf-8"
        return BeautifulSoup(data.text, "html5lib")

    except Exception as ex:
        return None


def GetSoup(url):
    try:
        data = requests.get(url)
        data.encoding = "utf-8"
        return BeautifulSoup(data.text, "html5lib")

    except Exception as ex:
        return None