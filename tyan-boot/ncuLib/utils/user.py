import requests
from bs4 import BeautifulSoup
from PIL import Image
from os import remove
from pytesseract import image_to_string
from utils import lib_db
from hashlib import md5

index_url = 'http://210.35.251.243/reader/login.php'
capture_url = 'http://210.35.251.243/reader/captcha.php'
login_url = 'http://210.35.251.243/reader/redr_verify.php'

salt = "QWDRhw"


def before_login():
    data = requests.get(index_url)
    data.encoding = 'utf-8'

    return data.cookies


def get_capture(cookies):
    data = requests.get(capture_url, cookies=cookies)
    with open("./img_cache/" + cookies['PHPSESSID'] + ".gif", "wb+") as f:
        f.write(data.content)

    gif = Image.open("./img_cache/" + cookies['PHPSESSID'] + ".gif")

    png = Image.new("RGB", gif.size)
    png.paste(gif)

    str = image_to_string(png).strip()
    remove("./img_cache/" + cookies['PHPSESSID'] + ".gif")

    return str


def login(user, passwd):
    cookies = before_login()

    chk_code = get_capture(cookies)

    post_data = {
        'number': user,
        'passwd': passwd,
        'captcha': chk_code,
        'select': 'cert_no',
        'returnUrl': ''
    }

    data = requests.post(login_url, cookies=cookies, data=post_data)
    data.encoding = 'utf-8'

    soup = BeautifulSoup(data.text, "html5lib")

    status = soup.select(".header_right_font")[1].find_all("a")[1].text

    if status == "注销":
        status = True
        if has_user(user) is False:
            print("succ")
            add_user(user)
    else:
        status = False

    ret_data = {'status': status,
                'cookies': {
                    'PHPSESSID': cookies['PHPSESSID'],
                    'USERID': md5((user + salt).encode("utf-8")).hexdigest(),
                    'USER': user
                }
                }

    return ret_data


# check if a user has login before
def has_user(user):
    db_con = lib_db.init_db()
    cur = db_con.cursor()

    sql = "SELECT `user` FROM user WHERE `user` = ?"

    r = cur.execute(sql, (user,))
    db_con.commit()
    data = r.fetchall()

    cur.close()
    db_con.close()
    return len(data) != 0


def add_user(user):
    db_con = lib_db.init_db()
    cur = db_con.cursor()

    sql = "INSERT INTO user (user) VALUES (?)"

    print(sql)
    cur.execute(sql, (user,))
    db_con.commit()
    cur.close()
    db_con.close()


def is_login(cookies):
    if "USER" not in cookies and "USERID" not in cookies:
        return False
    else:
        user = cookies["USER"]
        userid = cookies["USERID"]
        if not has_user(user):
            return False
        else:
            if md5((user + salt).encode("utf-8")).hexdigest() == userid:
                return True
            else:
                return False
