from flask import Blueprint,render_template,request,redirect,url_for
from database import get_db

member_bp=Blueprint("member",__name__,url_prefix="/member")

@member_bp.route("/books")
def books():
    db=get_db()
    cur=db.execute("SELECT * FROM books")
    books=cur.fetchall()
    return render_template("member/books.html",books=books)

