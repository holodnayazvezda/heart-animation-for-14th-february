from flask import Flask, render_template

app = Flask("heart server")


@app.route('/heart')
def hello():
    return render_template("index.html")
    # return "hello"

app.run(host='0.0.0.0', port=8080)