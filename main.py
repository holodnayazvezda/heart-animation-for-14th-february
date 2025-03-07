from flask import Flask, render_template

app = Flask("heart server")


@app.route('/love-with-compliments')
def love_with_compliments():
    return render_template("index-with-text.html")

@app.route('/love-with-emojis')
def love_with_emojis():
    return render_template("index-without-text.html")


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)