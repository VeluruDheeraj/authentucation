from flask import request, render_template, redirect, session
from database import get_db
import bcrypt

def register_auth_routes(app):

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"].encode()

            db = get_db()
            user = db.execute(
                "SELECT * FROM users WHERE username = ?",
                (username,)
            ).fetchone()

            if user and bcrypt.checkpw(password, user["password"]):
                session["user_id"] = user["id"]
                session["role"] = user["role"]

                if user["role"] == "admin":
                    return redirect("/admin/dashboard")
                return redirect("/member/dashboard")

        return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["username"]
            password = bcrypt.hashpw(
                request.form["password"].encode(),
                bcrypt.gensalt()
            )
            role = request.form["role"]

            db = get_db()
            db.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, password, role)
            )
            db.commit()
            return redirect("/login")

        return render_template("register.html")

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect("/login")