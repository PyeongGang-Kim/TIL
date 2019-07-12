from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:df>')
def cube(df):
    result=df**3
    return render_template('cube.html',result=result, number=df)

@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '비스트', '기생충', '알라딘', '라이온 킹', '마담싸이코']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age= request.args.get('age')
    return render_template('pong.html', age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')
