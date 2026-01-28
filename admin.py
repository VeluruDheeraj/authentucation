from flask import Blueprint,render_template,request,redirect,url_for
from database import get_db

admin_bp=Blueprint("admin",__name__,url_prefix="/admin")

@admin_bp.route("/books",methods=["GET","POST"])
def books():
    db=get_db()
    if request.method=="POST":
        title=request.form["title"]
        author=request.form["author"]

        db.execute(
            "INSERT INTO books (title,author,available) VALUES(?,?,?)",(title,author,1)
        
        )
        db.commmit()
        return redirect(url_for("admin.books"))
    cur=db.execute("SELECT * FROM BOOKS")
    books=cur.fetchall()
    return render_template("admin/books.html",books=books)
