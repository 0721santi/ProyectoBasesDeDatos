from flask import Flask, jsonify, request, render_template
from NoSQL import NoSQL

if __name__ == "__main_":
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    app.run(debug=True,)
    nosql = NoSQL()
    client = nosql.DBConn()