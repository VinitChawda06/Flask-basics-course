from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexflask.html')

@app.route('/route')
def report():
    
    lower = False
    upper = False
    num_end = False
    username = request.args.get('Username')

    lower = any(c.islower() for c in username)
    upper = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    report = lower and upper and num_end

    return render_template('reportflask.html',lower = lower, upper = upper, 
                             num_end = num_end, report = report)

if __name__== "__main__":
    app.run(debug=True)