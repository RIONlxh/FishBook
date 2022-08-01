def is_keyword_or_isbn(word):
    key = 'keyword'
    if len(word) == 13 and word.isdigit():
        key = 'keyword'
    if len(word.replace("-", "")) == 10 and word.replace("-", "").isdigit():
        key = 'isbn'
    return key
