from flask import jsonify

from handler import is_keyword_or_isbn
from main import app
from yushu_book import YuShu


@app.route('/search/<q>/<page>')
def search(q,page):
    keyword = is_keyword_or_isbn(q)
    if keyword == 'isbn':
        result = YuShu.search_by_isbn(q)
    else:
        result = YuShu.search_by_keyword(q)
    return jsonify(result)