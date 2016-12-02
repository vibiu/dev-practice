import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from worm_script.worm import Worm
from database import db_session
from models import List, User

HOST = "smtp.qq.com"
PORT = "587"
USERNAME = "2963103258@qq.com"
PASSWORD = "xjbiflstjpgldcfd"
DATABASE_URL = "mysql+pymysql://root:tjq980303@localhost:3306/library?charset=utf8"


old_time = time.time()
worm = Worm()


def send_email(from_addr, to_addr, text):
    smtp = smtplib.SMTP(HOST, PORT)
    smtp.starttls()
    smtp.login(USERNAME, PASSWORD)
    message = MIMEText(text)
    message["From"] = Header(from_addr, "utf-8")
    message["To"] = Header(to_addr, "utf-8")
    message["Subject"] = Header("notice", "utf-8").encode()
    smtp.sendmail(from_addr, to_addr, message.as_string())
    smtp.close()


def notice():
    q = db_session.query(List).all()
    for x in q:
        results = worm.get_book_info(strText=x.book_id)
        if "可借复本：0" not in results[0]["stock"]:

            send_email(from_addr=USERNAME, to_addr=db_session.query(User.id).filter(x.user_id).first(), text=x.book_id+"已经可借")
if __name__ == "__main__":
    while True:
        new_time = time.time()
        if new_time - old_time >= 36000:
            old_time = new_time
            print("send email")
            notice()
        time.sleep(10000)
