from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello World!'

@app.route('/Dojo')
def Dojo():
    return 'Dojo'

@app.route('/Hi/<string:say>')
def hi(Hi,say):
    return f"Hi, {say}"

@app.route('/<int:n>/<string:word>')
def words(word,n):
    return f"{word*n}"

if __name__ =="__main__":
    app.run(debug=True)