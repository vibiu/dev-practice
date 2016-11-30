#Ncu Library

A web app to search books on ncu library

#Important!
NOW ONLY API, NO VIEW

#Demo
Auto build by daocloud

[Demo](http://boot-nculib.daoapp.io)

[Search "Java" page 1 demo](http://boot-nculib.daoapp.io/api/books/java?page=1)


#API

##Search for books

GET /api/books/what-you-want-to-search?page=N

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "pages": 1,
    "ret_num": 3,
    "total_num": 3,
    "books": [
        {
            "publisher": "机械工业出版社 2013",
            "total_books": 3,
            "available_books": 0,
            "book_id": "0000823362",
            "book_index": "TP301.6/180",
            "author": "(美) Thomas H. Cormen ... [等]著",
            "name": "算法导论"
        },
        ...
    ]
}
```

##Get Details

GET /api/details/the-book-id

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "book_id": "0000823362",
    "total": 3,
    "available": 0,
    "books_status": [
        {
            "bar_code": "AN1454232",
            "status": "借出-应还日期：2016-11-10",
            "search_index": "TP301.6/180",
            "year": "-",
            "location": "前湖校区—前湖-流通书库"
        },
        {
            "bar_code": "AN1454233",
            "status": "借出-应还日期：2016-12-19",
            "search_index": "TP301.6/180",
            "year": "-",
            "location": "前湖校区—前湖-流通书库"
        },
        {
            "bar_code": "AN1454231",
            "status": "阅览",
            "search_index": "TP301.6/180",
            "year": "-",
            "location": "前湖校区—前湖-单本书阅览室"
        }
    ]
}
```

##Login

POST /api/login

```
POST /api/login HTTP/1.1
Content-Type: application/jose+json

{
    "user":"username",
    "password":"passwd"
}
```


```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "cookies": "PHPSESSID=1234567890abcdefghjiklmnop"
    "status": true
}
```