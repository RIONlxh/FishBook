from http_handler import HTTP


class YuShu:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}&cat=1001"
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    douban_book_url = 'https://search.douban.com/book/subject_search?search_text={}'

    @classmethod
    def search_by_keyword(cls, keyword, count=20, start=0,return_json=False):
        url = cls.douban_book_url.format(keyword)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result
