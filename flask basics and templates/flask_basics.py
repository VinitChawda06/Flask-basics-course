from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello Puppy!</h1>"
#Adding multiple pages using "/(name of page)" eg below
@app.route('/info')
def info():
    return "<h1> Entered in a new page!</h1>"

if __name__ == '__main__':
    app.run()