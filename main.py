from flask import Flask, jsonify, request, render_template
from NoSQL import NoSQL

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route('/')
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)