from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Vinit"
    ls = [5,6,7,8,9]
    name_ls = ["Vinit","Vivek","vibhanshu"]
    name_dict = {'Vinit':1}
    user_logged_in = True
    return render_template('basic.html', name=name, ls=ls, name_dict=name_dict, name_ls=name_ls, user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug= True)