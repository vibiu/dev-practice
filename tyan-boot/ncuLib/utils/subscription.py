import utils.lib_db as lib_db


def add(user, book_id):
    db_con = lib_db.init_db()
    cur = db_con.cursor()
    sql = "INSERT INTO subscriptions (user, subscription) VALUES (?, ?)", (user, book_id)

    cur.execute(sql)
    cur.close()
    db_con.commit()
    db_con.close()


def del_subs(user, book_id):
    db_con = lib_db.init_db()
    cur = db_con.cursor()

    sql = "UPDATE subscriptions SET is_del = 1 WHERE subscription =? AND user=?", (book_id, user)

    cur.execute(sql)

    cur.close()
    db_con.commit()
    db_con.close()
