from flask import Flask, render_template, request, redirect
from werkzeug.datastructures import Accept
app = Flask(__name__)


@app.route('/')
def form():
    return render_template("index.html")


@app.route('/submit', methods=["POST"])
def submit():
    print(request.form)
    namefrom = request.form['name']
    langfrom = request.form['language']
    locfrom = request.form['location']
    comfrom = request.form['comment']
    radio = request.form['radios']

    try:
        checked = request.form['checked']
        return render_template("submit.html", radio=radio, name=namefrom, location=locfrom, checked=checked, language=langfrom, comment=comfrom)

    except:
        return render_template("submit.html", radio=radio, name=namefrom, location=locfrom, language=langfrom, comment=comfrom)


if __name__ == "__main__":
    app.run(debug=True)
