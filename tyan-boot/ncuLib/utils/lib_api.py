import utils.lib_http as lib_http
import utils.subscription as subscription

query_para2 = {
    'dept': 'ALL',
    'displaypg': 50,
    'doctype': 'ALL',
    'lang_code': 'ALL',
    'match_flag': 'forward',
    'onlylendable': 'no',
    'orderby': 'DESC',
    'page': 1,
    'showmode': 'list',
    'sort': 'CATA_DATA',
    'title': 'c++',
    'with_ebook': 'on',
}

query_url = 'http://210.35.251.243/opac/openlink.php'
location_url = 'http://210.35.251.243/opac/ajax_item.php?marc_no='


def api_search(name, page=1):
    ret_data = {'books': []}
    query_para2['page'] = page
    query_para2["title"] = name

    soup = lib_http.GetSoupWithPara(query_url, query_para2)

    if soup is None:
        return {'err': 1, 'msg': "request error"}

    if len(soup.select(".search_form.bulk-actions")) > 0:
        total_num = int(soup.select(".search_form.bulk-actions")[0].p.strong.text)
    else:
        return {'err': 2, 'msg': "search empty"}

    if total_num is None:
        print("total none")
        return {'err': 3, 'msg': "search empty"}

    ret_data["total_num"] = total_num
    ret_data["ret_num"] = 0
    ret_data["pages"] = int(total_num / 50) + 1

    books = soup.select("ol")
    if len(books) is 0:
        return {'err': 4, 'msg': "parse error"}

    if len(books) == 0:
        return {'err': 6, 'msg': "search item error"}
    else:
        books = books[0].find_all("li")
        if len(books) == 0:
            return {'err': 5, 'msg': "search list error"}
        else:
            ret_data["ret_num"] = len(books)

            for book in books:
                book_json = {}

                total_books = int(book.p.span.next.strip()[5:])
                available_books = int(book.p.span.next.next.next.strip()[5:])
                book_index = book.h3.a.next.next.strip()

                book_json["name"] = book.h3.a.text.split(".")[1]
                book_json["available_books"] = available_books
                book_json["total_books"] = total_books
                book_json["book_index"] = book_index
                book_json["book_id"] = book.a.attrs["href"][-10:]
                book_json["publisher"] = book.p.contents[4].strip()
                book_json["author"] = book.p.contents[2].strip()

                ret_data["books"].append(book_json)

                print("%s %s/%s" % (book.h3.a.text.split(".")[1], available_books, total_books))

    return ret_data


def api_details(book_id):
    books_status = {'book_id': book_id,
                    'books_status': [],
                    'total': 0,
                    'available': 0}

    soup = lib_http.GetSoup(location_url + book_id)

    books = soup.table.find_all("tr")
    del (books[0])

    books_status["total"] = len(books)

    for book in books:
        book_status = {}
        book = book.find_all("td")

        book_status["search_index"] = book[0].text.strip()
        book_status["bar_code"] = book[1].text.strip()
        book_status["year"] = book[2].text.strip()
        book_status["location"] = book[3].text.strip()
        book_status["status"] = book[4].text.strip()

        if book_status["status"] == "可借":
            books_status["available"] += 1

        books_status["books_status"].append(book_status)

    return books_status


def api_add_subs(user, book_id):
    # TODO: XSS check
    subscription.add(user, book_id)


def api_del_subs(user, book_id):
    # TODO: XSS check
    subscription.del_subs(user, book_id)
