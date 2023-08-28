import sqlite3
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS bank(
            date text,
            naration text,
            debit text,
            credit text,
            currbalance text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def deposit(self,date,amount,cb):
        t="DEPOSIT"
        self.cur.execute("insert into bank values (?,?,NULL,?,?)",
                         (date,t,amount,cb))
        self.con.commit()

    def withdraw(self,date,amount,cb):
        t="WITHDRAW"
        self.cur.execute("insert into bank values (?,?,?,NULL,?)",
                         (date,t,amount,cb))
        self.con.commit()
    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from bank")
        date="date"
        naration="naration"
        debit="debit"
        credit="credit"
        cb="cb"
        print(f"{date: ^10} {naration: ^10} {debit: ^10} {credit: ^10} {cb: ^10}")
        rows = self.cur.fetchall()
        for i in rows:
            for j in i:
                if j == "":
                    print(f"{'': ^10}",end="")
                else:
                    print(f"{j:^10}",end="")
        
        # return rows
    def last(self):
        self.cur.execute("SELECT * from bank")
        rows = self.cur.fetchall()
        return rows
        
    def drop(self):
        self.cur.execute("DROP table bank")

    