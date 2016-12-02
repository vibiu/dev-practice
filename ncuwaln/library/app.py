from flask import Flask, request, session, jsonify, url_for, render_template
from database import db_session
from models import List, User
from worm_script.worm import Worm
import requests


app = Flask(__name__)
app.config.from_object("conf")


@app.route("/login")
def do_login():
    username = request.form["username"]
    password = request.form["password"]
    worm = Worm()
    response = requests.get(worm.img_url)
    res = worm.login(username=username, password=password, cookie=response.cookies, image=response.content)
    if res:
        if db_session.query(User).filter(User.id == username).first() is not None:
            db_session.add(User())
            db_session.commit()
        session["user_id"] = username
        return render_template("")
    else:
        return jsonify(message="login fail")


@app.route("/subscriptions/add", methods=["POST"])
def add_subscriptions():
    email = db_session.query(User).filter(User.id == request.form["user_id"]).first()
    if email is None:
        return jsonify(dict(message="no email"))
    book_id = request.form["book_id"]
    user_id = session["user_id"]
    try:
        db_session.add(List(email, book_id, user_id))
        db_session.commit()
        return jsonify(dict(message="add successful"))
    except:
        db_session.rollback()
        return jsonify(dict(message="add fail"))


@app.route("/subscriptions/delete", methods=["POST"])
def delete_subscriptions():
    id = request.form["id"]
    try:
        db_session.query(List).filter(List.id == id).delete()
        db_session.commit()
        return jsonify(dict(message="delete successful"))
    except:
        db_session.rollback()
        return jsonify(dict(message="delete fail"))


@app.route("/subscriptions/get")
def get_subscriptions_info():
    user_id = session["user_id"]
    if user_id is None:
        return jsonify(dict(message="no user"))
    query = db_session.query(List).filter(List.user_id == user_id).all()
    results = []
    for x, element in enumerate(query):
        results.append({
            x: element.get_dict()
        })
    return jsonify(results=results)


@app.route("/search", methos=["POST"])
def search():
    worm = Worm()
    title = request["title"]
    results = worm.get_book_info(strText=title)
    return jsonify(results=results)


if __name__ == "__main__":
    app.run()
