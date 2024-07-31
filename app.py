from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    """ipl project webpage to learn and experiment with bootstrap"""
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
