from flask import render_template, request, redirect, session
from database import get_db

def register_admin_routes(app):

    @app.route("/admin/dashboard")
    def admin_dashboard():
        if session.get("role") != "admin":
            return redirect("/login")
        return render_template("admin/dashboard.html")

    @app.route("/admin/books", methods=["GET", "POST"])
    def admin_books():
        if session.get("role") != "admin":
            return redirect("/login")

        db = get_db()

        if request.method == "POST":
            title = request.form["title"]
            author = request.form["author"]

            db.execute(
                "INSERT INTO books (title, author, available) VALUES (?, ?, ?)",
                (title, author, 1)
            )
            db.commit()
            return redirect("/admin/books")

        books = db.execute("SELECT * FROM books").fetchall()
        return render_template("admin/books.html", books=books)