from flask import Flask,Response

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    return Response("ok")

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'],host="0.0.0.0")

