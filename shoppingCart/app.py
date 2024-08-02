from flask import Flask, request, render_template,redirect, session
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///store.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET","POST"])
def index():
    books = db.execute("select * from books")
    return render_template("books.html", books=books)

@app.route("/cart", methods=["GET","POST"])
def cart():
    #ensure cart exists
    if "cart" not in session:
        session["cart"] = set()

    #post
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            #session["cart"].append(book_id)
            session["cart"] = list(set(session["cart"]) | {book_id})
        return redirect("/cart")

    #get
    #books = db.execute("select * from books where id in (?)", session["cart"])
    books = db.execute("SELECT * FROM books WHERE id IN (:cart)", cart=session["cart"])
    return render_template("cart.html", books=books)


#clear cookies
@app.route("/clear_cart", methods=["POST"])
def clear_cart():
    # Clear the cart by removing it from the session
    session.pop("cart", None)
    return redirect("/")

#@app.route("/login", methods=["POST","GET"])
#def login():
#    if request.method == "POST":
#        session["name"] = request.form.get("name")
 #       return redirect("/")
 #   return render_template("/login.html")


#@app.route("/logout")
#def logout():
#    session.clear()
#    return redirect("/")
