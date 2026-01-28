from flask import Flask, render_template, request, redirect, url_for, make_response, abort, g,Blueprint
import jwt, datetime, sqlite3, bcrypt
from functools import wraps
from database import init_db,close_db
from admin import admin_bp
from member import member_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key"


app.register_blueprint(admin_bp)
app.register_blueprint(member_bp)


@app.teardown_appcontext
def teardown_db(e=None):
    close_db(e)

if __name__=="__main__":
    init_db()
    app.run(debug=True)

