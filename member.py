from flask import render_template, redirect, session
from database import get_db

def register_member_routes(app):

    @app.route("/member/dashboard")
    def member_dashboard():
        if session.get("role") != "member":
            return redirect("/login")
        return render_template("member/dashboard.html")

    @app.route("/member/books")
    def member_books():
        if session.get("role") != "member":
            return redirect("/login")

        db = get_db()
        books = db.execute("SELECT * FROM books").fetchall()
        return render_template("member/books.html", books=books)
