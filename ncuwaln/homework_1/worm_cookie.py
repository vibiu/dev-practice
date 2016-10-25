import re
from selenium import webdriver

url = "http://222.204.3.49:8082/"
PhantomJS_path = "/usr/local/phantomjs-2.1.1-linux-x86_64/bin/phantomjs"


driver = webdriver.PhantomJS(PhantomJS_path)
# get yzm from cookie
def get_yzm():
    cok = driver.get_cookie("validateCookie")["value"]
    val = re.match(r"ChkCode=([1234567890qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYYHNUJMIKLOP]*)", cok)
    return val.group(1)

def get_page():
    driver.get(url)
    Txt_Yzm = get_yzm()
    driver.find_element_by_id("Txt_UserName").send_keys("8000115110")
    driver.find_element_by_id("Txt_PassWord").send_keys("8000115110")
    driver.find_element_by_id("Txt_Yzm").send_keys(Txt_Yzm)
    driver.find_element_by_id("Btn_login").click()
    return driver.page_source
