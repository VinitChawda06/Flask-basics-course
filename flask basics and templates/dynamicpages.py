from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello Puppy!</h1>"
#Adding multiple pages using "/(name of page)" eg below
@app.route('/info')
def info():
    return "<h1> Entered in a new page!</h1>"

@app.route('/String/<name>')
def admin(name):
    return "<h1>The 23rd letter of the given string is: {}</h1>".format(name[23])

if __name__ == '__main__':
    app.run(debug=True)