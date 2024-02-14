from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template('index.html')

@app.route("/success/<int:score>")
def success(score):
    return render_template('result.html',result = score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html',result = score)

@app.route("/submit", methods=["POST","GET"])
def submit():
    total_score= 0
    if request.method=='POST':
        python = float(request.form['Python'])
        c = float(request.form['C'])
        java = float(request.form['Java'])
        total_score= (python+c+java)/3
    res =""
    if total_score >= 50:
        res = "success"
    else:
        res = "fail"
    return redirect(url_for(res,score = total_score))


if __name__=='__main__':
    app.run(debug=True)