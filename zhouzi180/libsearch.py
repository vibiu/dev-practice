import requests
from bs4 import BeautifulSoup
import json
from flask import *

app = Flask(__name__)

serach_url = "http://opac.ncu.edu.cn/opac/openlink.php"


query_para2 = {
    'dept': 'ALL',
    'displaypg': 20,
    'doctype': 'ALL',
    'lang_code': 'ALL',
    'match_flag': 'forward',
    'onlylendable': 'no',
    'orderby': 'DESC',
    'page': 1,
    'showmode': 'table',
    'sort': 'CATA_DATA',
    'title': 'java',
    'with_ebook': 'on',
}


def api_search(name, page=1):
    book_num = {'books': []}
    query_para2['page'] = page
    query_para2['title'] = name

    books = requests.get(serach_url, query_para2)
    books.encoding = 'utf-8'
    soup = BeautifulSoup(books.text, "html5lib")
    books = soup.find_all("tr")
    for book in books:
        book_json = {}
        book1 = book.find_all("td")
        book_json["id"] = book1[0].text
        book_json["name"] = book1[1].text
        book_json["author"] = book1[2].text
        book_json["publisher"] = book1[3].text
        book_json["book_id"] = book1[4].text
        book_json["book_type"] = book1[5].text
        book_num['books'].append(book_json)
        print book
    return book_num

#@app.route('/<book>', defaults={'page' : 1})


@app.route('/<book>')
def index(book):
    page = request.args.get('page', None)

    if page == None:
        page = 1

    a = api_search(book, page)
    return jsonify(a)


app.run(debug=True)
