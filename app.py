from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h>Hello World !!!</h>"

@app.route("/<msg>", methods=["GET"])
def welcome(msg):
    return f"<h>Hello World !! {msg}!!!</h>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)