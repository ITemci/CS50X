from cs50 import SQL

db = SQL("sqlite:///dna.db")

name = input("Name: ")

rows = db.execute("select * from dna where name = ?", name)
#row = rows[0]
print(rows)
