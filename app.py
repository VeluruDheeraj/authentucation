from flask import Flask, render_template, request, redirect, url_for, make_response, abort, g
import jwt, datetime, sqlite3, bcrypt
from functools import wraps
from database import init_db,close_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key"





@app.teardown_appcontext
def teardown_db(e=None):
    close_db(e)

if __name__=="__main__":
    init_db()
    app.run(debug=True)

