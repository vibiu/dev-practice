import utils.lib_db as lib_db
from cron import celery_task


def run():
    db = lib_db.init_db()
    cur = db.cursor()

    subs_list = []
    data = cur.execute("""SELECT user.user as user, subscriptions.subid, subscriptions.user as suser,
 subscriptions.subscription, subscriptions.is_del, subscriptions.book_name FROM subscriptions LEFT JOIN user ON
 user.uid=subscriptions.user;""")
    data = data.fetchall()

    for item in data:
        subs_list.append(item[3])

    subs_list = list(set(subs_list))

    for book in subs_list:
        celery_task.check_details.delay(book)


def check_user():
    db = lib_db.init_db()
    cur = db.cursor()

    users = cur.execute("""SELECT * FROM user""").fetchall()
    db.commit()

    for user in users:

        user_id = user[1]
        subs = cur.execute("""SELECT * FROM subscriptions WHERE is_del = 0 AND user = ?""", (user_id,))
        subs = subs.fetchall()

        if len(subs) == 0:
            print("No subs")
            continue

        subs_li = []

        for sub in subs:
            sub_id = sub[2]
            subs_li.append(sub_id)

        subs_li = list(set(subs_li))
        celery_task.send_mail.delay(user_id, subs_li)
