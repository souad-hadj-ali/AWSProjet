from flask import (Flask, request, render_template)
import requests

app = Flask(__name__, static_url_path='/Image')


@app.route("/")
def hello():
    return "Running"


@app.route("/index")
def content():
    # Todo 1
    response = requests.get(url="http://3.72.85.29:3000/index")
    return render_template("index.html", response=response.text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
