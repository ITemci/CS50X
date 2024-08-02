import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# HOME
@app.route("/")
@login_required
def index():
    #stock = db.execute("select symbol from buy where user_id = ?",session["user_id"])
   # amount = db.execute("select amount from buy where user_id = ?", session["user_id"])
   # current_price = lookup(stock)
    #value = amount * current_price
   # balance = db.execute("select cash from users where id = ?", session["user_id"])
   # total_value = value + balance


    stocks= db.execute("select symbol, amount as total_shares from portfolio where user_id = ? group by symbol having total_shares > 0",session["user_id"])
    balance = db.execute("select cash from users where id = ?", session["user_id"])



    total_value = balance[0]["cash"] if balance else 0


    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["symbol"] = quote["symbol"]
        stock["price"] = quote["price"]
        stock["value"] = round(stock["price"] * stock["total_shares"],2)

        # Update total_value with the current stock's value
        total_value += stock["value"]



    return render_template("index.html", stocks=stocks, balance=round(balance[0]["cash"],2), total_value=round(total_value,2))


    #return render_template("index.html", stocks=stocks,balance=balance[0]["cash"],quote=quote["price"])

# BUY
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Please introduce symbol name")
        stock = lookup(symbol)
        if stock == None:
            return apology("Company not found!")
        elif not shares.isdigit() or int(shares) < 1:
            return apology("Amount is not a number or is less than 1")

        shares= int(shares)
        stock_price = stock["price"]
        # getting the amount of cash available to user
        cash = db.execute("select cash from users where id = ?", session["user_id"])

        # checking if user had enough cash to buy stock
        if cash[0]["cash"] < stock_price * shares:
            return apology("Not enough money")
        else:
            db.execute("insert into buy(user_id,symbol,price,amount) values(?,?,?,?)", session['user_id'],symbol,stock_price,shares )
            new_cash = cash[0]["cash"] - stock_price * shares
            db.execute("update users set cash=? where id=?",new_cash,session['user_id'])

            # updating porfolio
            rowExist = db.execute("select * from portfolio where user_id = ? and symbol = ?",session["user_id"], symbol)
            if rowExist:
                new_amount = rowExist[0]["amount"] + int(shares)
                db.execute("update portfolio set amount = ? where symbol = ? and user_id=?",new_amount,symbol,session["user_id"])
            else:
                db.execute("insert into portfolio values(?,?,?)",session["user_id"],symbol,shares)

            total_cost = shares * stock_price
            flash(f"Bought {shares} shares of {symbol} for {usd(total_cost)}!")
            return redirect("/")



# HISTORY
@app.route("/history")
@login_required
def history():
    union = db.execute("select * from buy where user_id = ? union select * from sell where user_id = ?",session["user_id"],session["user_id"])
    return render_template("history.html",union=union)

# LOG IN
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["user_name"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# LOG OUT
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# QUOTE
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method== "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please introduce symbol name")
        stock = lookup(symbol)
        if stock == None:
            return apology("Company not found!")
        stock_symbol = stock["symbol"]
        stock_price = stock["price"]
        return render_template("quoted.html",stock_symbol=stock_symbol,stock_price=stock_price)

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        hashed = generate_password_hash(password, method='pbkdf2', salt_length=16)

         # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username
        )

        if not username:
            return apology("must provide username", 400)
        elif len(rows)==1:
            return apology("Username already exists", 400)
        elif not password:
            return apology("must provide password", 400)
        elif password != confirmation:
            return apology("passwords do not match",400)
        else:
            db.execute("insert into users(username,hash) values(?,?)",username,hashed)


        return render_template("login.html")

# SELL
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    if request.method == "GET":
        stocks = db.execute("select * from portfolio where user_id = ?",session["user_id"])
        return render_template("sell.html",stocks=stocks)
    else:
        stocks = db.execute("select * from portfolio where user_id = ?",session["user_id"])
        shares = request.form.get("shares")
        stock = request.form.get("symbol")
        if not stock:
            return apology("Please select stock you want to sell !!!")
        elif not shares.isdigit() or int(shares) < 1:
            return apology("Amount is not a number or is less than 1")

        selected_stock = None
        for i in stocks:
            if stock == i["symbol"]:
                selected_stock = i
                break

        if selected_stock["amount"] < int(shares):
            return apology("You dont own this many shares !!!")

        #inserting into sell table
        s = lookup(stock)
        db.execute("insert into sell(user_id,symbol,sold_price,amount_sold) values(?,?,?,?)",session["user_id"],stock,s["price"],shares)

        #updateing table porfolio
        portfolio = db.execute("select * from portfolio where user_id = ? and symbol=?",session["user_id"],selected_stock["symbol"])
        new_amount = portfolio[0]["amount"] - int(shares)
        db.execute("update portfolio set amount = ? where symbol = ? and user_id=?",new_amount,stock,session["user_id"])


        return redirect("/")

@app.route("/changePassword",methods=["GET","POST"])
@login_required
def changePassword():
    if request.method == "GET":
        return render_template("changePassword.html")
    else:
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")



        if not password:
            return apology("must provide password", 403)
        elif password != confirmation:
            return apology("passwords do not match",403)
        else:
            hashed = generate_password_hash(password, method='pbkdf2', salt_length=16)
            db.execute("update users set hash = ? where id = ?",hashed,session["user_id"])
            return apology("Password changed successfuly")


@app.route("/top_up",methods=["POST"])
@login_required
def top_up():
    amount = request.form.get("top_amount")
    cash = db.execute("select cash from users where id = ?", session["user_id"])
    new_amount = float(amount) + cash[0]["cash"]
    db.execute("update users set cash = ? where id = ?", new_amount,session["user_id"])
    return redirect("/")

@app.route("/filter",methods=["POST"])
@login_required
def filter():
    filter = request.form.get("symbol")
    if filter == "Sell":
        union = db.execute("select * from sell where user_id = ?",session["user_id"])
        return render_template("sell_filter.html",union=union)
    elif filter == "Buy":
        union = db.execute("select * from buy where user_id = ?",session["user_id"])
        return render_template("history.html",union=union)
    else:
        return redirect("/history")

