from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return"<h1>Welcome ! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

@app.route('/puppy_latin/<name>')
def puppy(name):
    if name.lower()[-1]== 'y':
        return f"<h1>Hi {name} !Your puppy latin name is {name[:-1]}iful</h1>"
    else:
        return f"<h1>Hi {name} !Your puppy latin name is {name}y</h1>"

if __name__ == '__main__':
    app.run()