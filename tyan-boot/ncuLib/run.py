#!/bin/python

# -*- coding:utf-8 -*-

from flask import Flask, request, jsonify, make_response, redirect, render_template
import json
from utils import user
from utils import lib_api

app = Flask(__name__)
app.jinja_env.variable_start_string = '{{{'
app.jinja_env.variable_end_string = '}}}'


@app.route('/api/books/<string:name>')
def api_search(name):
    if request.args.get("page") is not None:
        page = request.args.get("page")
    else:
        page = 1

    ret_data = lib_api.api_search(name, page)

    return jsonify(ret_data)


@app.route('/api/details/<string:book_id>')
def api_details(book_id):
    books_status = lib_api.api_details(book_id)

    return jsonify(books_status)


@app.route('/api/login', methods=["POST"])
def api_login():
    json_data = request.get_json()

    if json_data is not None:
        if "user" in json_data:
            user_name = json_data["user"]
        else:
            return jsonify(err=9, msg="username required")

        if "password" in json_data:
            pwd = json_data["password"]
        else:
            return jsonify(err=9, msg="password required")

        data = user.login(user_name, pwd)

        response = make_response()
        if data["status"] is True:
            response.set_cookie("USER", data["cookies"]["USER"])
            response.set_cookie("USERID", data["cookies"]["USERID"])
            response.set_cookie("PHPSESSID", data["cookies"]["PHPSESSID"])

        response.mimetype = "application/json"
        response.data = json.dumps(data)

        return response
    else:
        return jsonify(err=9, msg="Post data error")


@app.route('/api/subs', methods=["POST"])
def add_sub():
    if user.is_login(request.cookies) is False:
        return jsonify(err=10, msg="no login")

    json_data = request.get_json()
    if "user" in json_data and "book_id" in json_data:
        lib_api.api_add_subs(json_data["user"], json_data["book_id"])
        return jsonify(err=0, msg="succ")
    else:
        return jsonify(err=1, msg="user or book_id error")


@app.route('/api/subs', methods=["DELETE"])
def del_sub():
    if user.is_login(request.cookies) is False:
        return jsonify(err=10, msg="no login")

    json_data = request.get_json()
    if "user" in json_data and "book_id" in json_data:
        lib_api.api_del_subs(json_data["user"], json_data["book_id"])
        return jsonify(err=0, msg="succ")
    else:
        return jsonify(err=1, msg="user or book_id error")


@app.route('/index')
@app.route('/')
def index():
    if user.is_login(request.cookies) is False:
        return redirect("/login")
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.errorhandler(405)
def MethodError(error):
    response = make_response()
    response.status_code = 405
    response.mimetype = "application/json"
    response.data = json.dumps({'err': 400, 'msg': "Method not allowed"})

    return response


@app.errorhandler(404)
def NotFound(error):
    err_msg = {
        'search book': "/api/books/book[?page=1]",
        'book details': "/api/details/book_id",
        'login': "/api/login"
    }
    response = make_response()
    response.status_code = 404
    response.mimetype = "application/json"
    response.data = json.dumps(err_msg)

    return response


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
