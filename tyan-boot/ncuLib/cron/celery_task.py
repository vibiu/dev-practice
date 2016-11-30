from celery import Celery
from utils import lib_api
from utils import lib_db

app = Celery("celery_task", backend="redis://localhost", broker="redis://localhost")


@app.task
def check_details(book_id):
    result = lib_api.api_details(book_id)
    available = result["available"]
    with lib_db.init_db() as db:
        cur = db.cursor()
        sql = """DELETE FROM details WHERE book_id = ? """
        cur.execute(sql, (str(book_id),))
        db.commit()

        sql = """INSERT INTO `details` (`book_id`, `available`) VALUES (?,?)"""
        cur.execute(sql, (book_id, available))
        cur.close()
        db.commit()


@app.task
def send_mail(user, subs):
    print("User : %s has : " % (user))
    print(subs)

    # TODO: send e-mail
    pass
